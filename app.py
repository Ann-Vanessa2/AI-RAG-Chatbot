# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# from ai import get_response  # Import AI function

# # Set Streamlit page config
# st.set_page_config(page_title="RAG Chatbot", layout="wide")

# # Stylish title
# st.markdown("<h1 style='text-align: center;'>💬 AI-Powered RAG Chatbot with Gemini</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; color: gray;'>Ask any question about Paul Graham's essay!</p>", unsafe_allow_html=True)

# # User imput
# user_query = st.text_input("💡 Enter your question:", placeholder="Type your question here...")

# # Spacing
# st.markdown("---")

# if st.button("🎤 Get Response"):
#     if user_query.strip():
#         response = get_response(user_query)  # Call AI function

#         # Check if response is empty
#         if response:
#             st.subheader("🤖 AI Response:")
#             # st.write(response)  # Ensure response is a string
#             st.write(f"<p style='font-size:16px;'>{response}</p>", unsafe_allow_html=True)  # Prevents Markdown formatting

#         else:
#             st.warning("⚠️ The AI did not return a response. Try asking differently.")
#     else:
#         st.warning("⚠️ Please enter a question before submitting.")


# # BASE
# import streamlit as st
# from ai import get_response  # Import AI function

# # Set Streamlit page config
# st.set_page_config(page_title="RAG Chatbot", layout="wide")

# # Custom CSS for styling
# st.markdown("""
#     <style>
#         .chat-container {
#             max-width: 700px;
#             margin: auto;
#         }
#         .user-message, .ai-message {
#             padding: 15px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#             display: flex;
#             align-items: center;
#         }
#         .user-message {
#             background-color: #f0f2f5;
#         }
#         .ai-message {
#             background-color: #fff;
#             border: 1px solid #ddd;
#         }
#         .icon {
#             font-size: 20px;
#             margin-right: 10px;
#         }
#         .input-container {
#             position: fixed;
#             bottom: 0;
#             width: 100%;
#             background: #f8f9fa;
#             padding: 10px;
#             display: flex;
#             align-items: center;
#             border-top: 1px solid #ddd;
#         }
#         .stTextInput > div > div > input {
#             width: 100%;
#             padding: 10px;
#             border-radius: 20px;
#             border: 1px solid #ddd;
#             outline: none;
#         }
#         .send-button {
#             background: none;
#             border: none;
#             font-size: 20px;
#             margin-left: 10px;
#             cursor: pointer;
#             color: gray;
#             transition: transform 0.2s;
#         }
#         .send-button.active {
#             color: #007bff;
#             cursor: pointer;
#             transform: scale(1.1);
#         }
#         /* Fix button alignment */
#         .send-button-col {
#             display: flex !important;
#             align-items: flex-start !important;
#             padding-left: 10px !important;
#             margin-top: 5px !important;
#         }
#         /* Adjust column widths */
#         .input-column {
#             max-width: 700px !important;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.title("💬 AI-Powered RAG Chatbot")
# st.markdown("<p style='text-align: center; color: gray;'>Ask any question about Paul Graham's essay!</p>", unsafe_allow_html=True)

# # Chat UI container
# st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# col1, col2 = st.columns([6.2, 0.8])
# with col1:
#     user_query = st.text_input("User Input", placeholder="Ask me anything about the essay", key="user_input", label_visibility="hidden")
# with col2:
#     st.markdown("<div class='send-button-col'>", unsafe_allow_html=True)
#     send_button = st.button("➤")
#     st.markdown("</div>", unsafe_allow_html=True)

# if send_button and user_query.strip():
#     st.markdown(f"""
#         <div class='user-message'>
#             <span class='icon'>💬</span> {user_query}
#         </div>
#     """, unsafe_allow_html=True)
    
#     response = get_response(user_query)
#     st.markdown(f"""
#         <div class='ai-message'>
#             <span class='icon'>🤖</span> {response}
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)



# import streamlit as st
# from ai import get_response  # Import AI function

# # Set Streamlit page config
# st.set_page_config(page_title="RAG Chatbot", layout="wide")

# # Custom CSS for styling
# st.markdown("""
#     <style>
#         /* Center the header */
#         .title {
#             text-align: center;
#             font-size: 36px;
#             font-weight: bold;
#         }
#         .subtitle {
#             text-align: center;
#             color: gray;
#             font-size: 16px;
#             margin-bottom: 20px;
#         }
        
#         /* Chat container */
#         .chat-container {
#             max-width: 700px;
#             margin: auto;
#         }
        
#         /* User & AI messages */
#         .user-message, .ai-message {
#             padding: 15px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#             display: flex;
#             align-items: center;
#         }
#         .user-message {
#             background-color: #ffefef;
#             border-left: 5px solid red;
#         }
#         .ai-message {
#             background-color: #fffbe6;
#             border-left: 5px solid orange;
#         }
        
#         /* Message icons */
#         .icon {
#             font-size: 20px;
#             margin-right: 10px;
#         }
        
#         /* Input field */
#         .input-container {
#             display: flex;
#             justify-content: space-between;
#             background: #f8f9fa;
#             padding: 10px;
#             border-radius: 10px;
#             border: 1px solid #ddd;
#             margin-top: 20px;
#         }
#         .stTextInput > div > div > input {
#             width: 100%;
#             padding: 10px;
#             border-radius: 20px;
#             border: none;
#             outline: none;
#         }
        
#         /* Send button */
#         .send-button {
#             background: none;
#             border: none;
#             font-size: 24px;
#             cursor: pointer;
#             color: gray;
#             transition: color 0.2s, transform 0.2s;
#         }
#         .send-button:hover {
#             color: #007bff;
#             transform: scale(1.1);
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Centered Header
# st.markdown("<h1 class='title'>💬 AI-Powered RAG Chatbot</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subtitle'>I am here to answer any questions you might have about Paul Graham's essay!</p>", unsafe_allow_html=True)

# # Chat UI container
# st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# # Chat input field & button
# col1, col2 = st.columns([6.2, 0.8])
# with col1:
#     user_query = st.text_input("User Input", placeholder="Ask me anything about the essay", key="user_input", label_visibility="hidden")
# with col2:
#     send_button = st.button("➤", help="Send Message", key="send_button")

# if send_button and user_query.strip():
#     st.markdown(f"""
#         <div class='user-message'>
#             <span class='icon'>💬</span> {user_query}
#         </div>
#     """, unsafe_allow_html=True)
    
#     response = get_response(user_query)
#     st.markdown(f"""
#         <div class='ai-message'>
#             <span class='icon'>🤖</span> {response}
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st
from ai import get_response  # Import AI function

# Set Streamlit page config
st.set_page_config(page_title="RAG Chatbot", layout="wide")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Custom CSS for styling
st.markdown("""
 <style>
             .chat-container {
            max-width: 70%;
            margin: auto;
            padding-bottom: 80px;
        }
        
        /* .user-message, .ai-message {
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
        } */

        /* Input Box Fixed at Bottom */
        .chat-bubble {
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            max-width: 80%;
        }       

        .user-message {
            background-color: #f0f2f5;
            /* recent change */
            align-self: flex-end;
        }
        .ai-message {
            background-color: #fff;
            border: 1px solid #ddd;
            align-self: flex-start;
        }
            
        .custom-input {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #ccc;
            font-size: 16px;
        }
        .custom-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 6px 20px;
            font-size: 18px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 27px;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Header (Centered)
st.markdown("<h2 style='text-align: center;'>💬 AI-Powered RAG Chatbot</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Ask any question about Paul Graham's essay!</p>", unsafe_allow_html=True)

# Chat History Container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Display previous chat history
# for chat in reversed(st.session_state.chat_history):
for chat in st.session_state.chat_history:
    st.markdown(chat, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# User Input and Send Button
# Fixed at Bottom
# st.markdown('<div class="input-container">', unsafe_allow_html=True)
# col1, col2 = st.columns([9, 1])
# with col1:
#     user_query = st.text_input("User Input", placeholder="Ask me anything...", key="user_input", label_visibility="hidden")
# with col2:
#     send_button = st.button("➤")
# st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([9, 1])
with col1:
    user_query = st.text_input("User Input", placeholder="Ask me anything...", key="user_input", label_visibility="hidden", help="Type your query here")
    # st.markdown('<input class="custom-input" type="text" value="' + user_query + '">', unsafe_allow_html=True)
with col2:
    # send_button = st.button("➤", key="send_button", help="Click to send", on_click=None)
    send_button = st.markdown('<button title="Click to send" class="custom-button">➤</button>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Process User Input
if send_button and user_query.strip():
    # # Display User Message
    # user_msg = f"<div class='user-message'><span class='icon'>💬</span> {user_query}</div>"
    # st.session_state.chat_history.append(user_msg)
    # st.markdown(user_msg, unsafe_allow_html=True)

    # Handle API Quota Exhaustion
    try:
        response = get_response(user_query)
    except Exception as e:
        response = "⚠️ API quota exceeded. Try again later."

    # # Display AI Response
    # ai_msg = f"<div class='ai-message'><span class='icon'>🤖</span> {response}</div>"
    # st.session_state.chat_history.append(ai_msg)
    # st.markdown(ai_msg, unsafe_allow_html=True) I

    # Append AI Response First
    ai_msg = f"<div class='chat-bubble ai-message'><span class='icon'>🤖</span> {response}</div>"
    st.session_state.chat_history.append(ai_msg)

    # Append User Message After AI Response
    user_msg = f"<div class='chat-bubble user-message'><span class='icon'>💬</span> {user_query}</div>"
    st.session_state.chat_history.append(user_msg)

    # Clear the input field
    del st.session_state["user_input"]

    # Refresh UI with new messages
    st.rerun()