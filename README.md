"# gen-ai-hackathon-research-paper-chatbot" 
# RE-Insight AI: Chat with PDFs and URLs

## Overview

RE-Insight AI is an interactive web application that allows users to chat with PDFs and URLs. It utilizes Google’s Generative AI to provide intelligent responses based on the content of uploaded PDF documents or provided URLs. The application supports processing multiple PDFs and URLs, making it a powerful tool for extracting insights from academic papers, research articles, and online content.

## Features

- **Chat Interface:** A user-friendly chat interface for interaction.
- **PDF Uploads:** Upload multiple PDF documents for analysis.
- **URL Processing:** Input multiple URLs for content retrieval.
- **Chat History:** Keeps a record of user and bot messages.
- **Custom Animations:** Smooth animations for message display.

## Technologies Used

- **Python:** The primary programming language for the application.
- **Streamlit:** For creating the web interface.
- **Google Generative AI:** To generate responses based on user queries.
- **NLTK:** For natural language processing tasks (if applicable).
- **dotenv:** For managing environment variables.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/re-insight-ai.git
   cd re-insight-ai
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory and add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. **Chat with PDFs and URLs:**
   - Upload your PDF files using the file uploader.
   - Enter URLs in the provided text area.
   - Ask questions in the input box to interact with the uploaded content.

4. Use the "New Chat" button in the sidebar to start a fresh conversation.

## File Structure

```
re-insight-ai/
│
├── src/
│   ├── document_processing.py    # Functions for PDF text extraction and chunking
│   ├── user_interface.py          # Functions for handling user input
│   ├── vector_store.py            # Functions for vector storage and retrieval
│   └── web_page_retrieval.py      # Functions for retrieving content from URLs
│
├── main.py                        # Main application script
├── requirements.txt               # List of required Python packages
└── .env                           # Environment variables
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to Google for providing the Generative AI API.
- Inspiration from the open-source community for tools and libraries used in this project.
