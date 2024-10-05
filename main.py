import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

from src.document_processing import get_pdf_text, get_text_chunks
from src.user_interface import user_input
from src.vector_store import get_vector_store
from src.web_page_retrieval import get_url_content

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set page config at the top
st.set_page_config("Chat with PDFs and URLs")

# Function to display chat history
def display_chat():
    st.sidebar.header("Chat History")
    for message in st.session_state['chat_history']:
        if message['role'] == 'user':
            st.sidebar.markdown(f"<div style='animation: fadeIn 0.5s;'><b style='color: blue;'>You:</b> {message['content']}</div>", unsafe_allow_html=True)
        elif message['role'] == 'bot':
            st.sidebar.markdown(f"<div style='animation: fadeIn 0.5s;'><b style='color: green;'>Bot:</b> {message['content']}</div>", unsafe_allow_html=True)

# Add custom CSS for animations
st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .message {
        transition: transform 0.3s ease;
    }
    .message:hover {
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.header("Chat with RE-Insight AI")

    # Initialize chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = ''

    # Add a button to clear chat and start a new conversation
    if st.sidebar.button("New Chat"):
        st.session_state['chat_history'] = []  
        st.session_state['user_input'] = ''    
        st.experimental_set_query_params()  # Refresh the app by resetting query parameters

    # Display chat history
    display_chat()

    # Ask a question input box
    user_question = st.text_input("Ask a question", key="user_input")

    if user_question:
        # Append user input to chat history
        st.session_state['chat_history'].append({'role': 'user', 'content': user_question})

        # Get the bot response using the user_input function
        bot_response = user_input(user_question)  # Ensure this function calls the API and gets a response

        if bot_response:  # Check if bot_response is not None or empty
            # Display the question and response
            st.markdown(f"<div class='message' style='background-color: #e1f5fe; padding: 10px; border-radius: 10px; margin: 5px 0;'>"
                        f"<b style='color: blue;'>You:</b> {user_question}</div>", unsafe_allow_html=True)

            st.markdown(f"<div class='message' style='background-color: #fff9c4; padding: 10px; border-radius: 10px; margin: 5px 0;'>"
                        f"<b style='color: green;'>Bot:</b> {bot_response}</div>", unsafe_allow_html=True)

            # Append the bot response to the chat history
            st.session_state['chat_history'].append({'role': 'bot', 'content': bot_response})

    with st.sidebar:
        st.header("Upload PDFs or enter URLs to process")
        st.markdown("---")

        # Section for PDF uploads
        try:
            pdf_docs = st.file_uploader("Upload your PDF files and Submit", accept_multiple_files=True)
            if st.button("Submit & Process PDFs"):
                with st.spinner("Processing PDFs..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("PDFs processed")
        except Exception as e:
            st.warning("Please upload a PDF file.")
            
        st.markdown("---")
        urls = st.text_area("Enter multiple URLs (one per line):")
        if st.button("Submit & Process URLs"):
            with st.spinner("Processing URLs..."):
                # Process multiple URLs
                url_contents = [get_url_content(url) for url in urls.splitlines()]
                all_text_chunks = [chunk for content in url_contents for chunk in get_text_chunks(content)]
                get_vector_store(all_text_chunks)
                st.success("URLs processed")
    
    

if __name__ == "__main__":
    main()
