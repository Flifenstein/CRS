import streamlit as st


st.set_page_config(
    page_title="Iris CRS",
    page_icon='💬',
    layout='wide'
)
st.header("Conversational Recommender System with Language Models and Langchain")

st.write("""
Welcome to our  Conversation Recommender System! 

We are delighted to have you as a participant in our user testing session. In this interactive experience, you will have the opportunity to engage with our chatbot on two intriguing tasks, each designed to showcase the versatility and utility of our system.

Task 1: Conversational Interaction

The first task invites you to engage in a conversation with our chatbot. Feel free to initiate a dialogue, ask questions, or explore various topics of interest. Our chatbot is here to provide informative and engaging responses. Additionally, if you ever wish to retrieve source links related to the conversation, you can simply ask, and our chatbot will assist you.

Task 2: Scientific Abstract Generation

In the second task, you will have the opportunity to harness the power of our system to generate scientific abstracts on any topic of your choosing. Share your chosen topic, and our chatbot will craft a concise and informative abstract for you. This task showcases the research and text generation capabilities of our system.

Using Your OpenAI Key

To ensure a seamless experience, you have the option to use your own OpenAI API key, allowing you to interact with our chatbot using your own resources. Alternatively, we can provide you with an OpenAI key for the duration of this session. The choice is yours, and we are here to assist you with either option.

Getting Started

To begin, please add the OpenAI key to your session. This key will enable our chatbot to access the necessary language models for generating responses. Once you've added the key, you can chat away for as long as you like, with a minimum recommended duration of 4 minutes.

Optional Recording

For your convenience, we have included an optional feature in the menu on the top right of your screen—a recording conversation option. If you wish to capture and review your interactions or share them with our researchers, you can simply activate this feature.

We appreciate your participation and value your feedback. Your insights and experiences will contribute to the refinement and enhancement of our chatbot and conversation recommender system. Thank you for being a part of this exciting journey, and we look forward to your engaging conversations and abstract generation sessions!





""")
