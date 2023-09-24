import os
import random
import streamlit as st


#decorator
def enable_chat_history(func):
    if os.environ.get("OPENAI_API_KEY"):

        # to clear chat history after swtching chatbot
        current_page = func.__qualname__
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = current_page
        if st.session_state["current_page"] != current_page:
            try:
                st.cache_resource.clear()
                del st.session_state["current_page"]
                del st.session_state["messages"]
            except:
                pass
    elif os.environ.get("HUGGINGFACEHUB_API_TOKEN"):
        # to clear chat history after swtching chatbot
        current_page = func.__qualname__
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = current_page
        if st.session_state["current_page"] != current_page:
            try:
                st.cache_resource.clear()
                del st.session_state["current_page"]
                del st.session_state["messages"]
            except:
                pass

        # to show chat history on ui
    if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "I am Iris, you research assistant. My end goal is to help you generate a scientific abstract. What topic would you like to chat about?"}]
    for msg in st.session_state["messages"]:
            st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute




def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    st.session_state.messages.append({"role": author, "content": msg})
    if author == "user":
        st.chat_message(author, avatar="🤗").write(msg)
    else:
        st.chat_message(author, avatar= "💡").write(msg)
  
   



def configure_openai_api_key():
    openai_api_key = st.sidebar.text_input(
        label="OpenAI API Key",
        type="password",
        value=st.session_state['OPENAI_API_KEY'] if 'OPENAI_API_KEY' in st.session_state else '',
        placeholder="sk-..."
        )
    if openai_api_key:
        st.session_state['OPENAI_API_KEY'] = openai_api_key
        os.environ['OPENAI_API_KEY'] = openai_api_key
    else:
        st.error("Please add your OpenAI API key to continue.")
        st.info("Obtain your key from this link: https://platform.openai.com/account/api-keys")
        st.stop()
    return openai_api_key

def configure_huggingface_api_key():
    hf_api_key = st.sidebar.text_input(
        label="HuggingFace API Key",
        type="password",
        value=st.session_state['HUGGINGFACEHUB_API_TOKEN'] if 'HUGGINGFACEHUB_API_TOKEN' in st.session_state else '',
        placeholder="hf-..."
        )
    if hf_api_key:
        st.session_state['HUGGINGFACEHUB_API_TOKEN'] = hf_api_key
        os.environ['HUGGINGFACEHUB_API_TOKEN'] = hf_api_key
    else:
        st.error("Please add your HuggingFace API key to continue.")
        st.info("Obtain your key from this link: https://huggingface.co/settings/profile ")
        st.stop()
    return hf_api_key


