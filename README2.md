# Chat with Website Content

This project enables users to interact with website content through an AI-powered question-answering system. The app scrapes textual content from a given URL, processes it, and allows users to ask questions based on the extracted data.

## Features

- **Web Scraping**: Extracts visible textual content from a website, ignoring scripts and styles.
- **AI Question-Answering**: Uses a large language model (LLM) to answer questions about the scraped content.
- **Vector Store**: Embeds website content into a searchable FAISS index for efficient information retrieval.
- **Streamlit UI**: User-friendly interface for URL input and interacting with the app.

## Requirements

To run this project, install the following Python libraries:
- `beautifulsoup4`
- `requests`
- `langchain`
- `streamlit`
- `faiss-cpu`


pip install beautifulsoup4 requests langchain streamlit faiss-cpu
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/chat-with-website-content.git
cd chat-with-website-content
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set your Groq API key in the code: Replace gsk_h0qbC8pOhPepI7BU0dtTWGdyb3FY........... with your actual API key.

How to Run
Start the Streamlit application:

bash
Copy code
streamlit run app.py
Open the app in your browser at http://localhost:8501.

Enter the URL of the website in the sidebar and click "Scrape Website."

Once the content is processed, ask questions in the input box, and the app will respond with answers based on the scraped content.

# Key Files
app.py: The main script containing the Streamlit app and processing logic.
faiss_store_website.pkl: Pickle file storing the FAISS vector index for retrieved embeddings.

## Functionality Breakdown
# Web Scraping
Fetches and parses website content using requests and BeautifulSoup.
Removes non-visible elements such as scripts and styles.
# Text Chunking
Splits the scraped content into manageable chunks for embedding.
# Vector Embedding
Generates embeddings using sentence-transformers for efficient search and retrieval.
# Retrieval-based QA
Employs LangChain's RetrievalQA to retrieve and answer questions using a pre-built vector index.
# Example Usage
Enter the URL of a blog or news article.
Ask, "What are the main points discussed?"
Get an AI-generated answer based on the scraped content.
Future Enhancements
Add support for handling dynamic websites (e.g., JavaScript-heavy pages).
Enable scraping of images and multimedia data.
Optimize content processing for large websites.

![Screenshot 2024-12-19 223752](https://github.com/user-attachments/assets/2e477af2-4c59-4d87-803a-f7cc5efb7b14)

![Screenshot 2024-12-19 223850](https://github.com/user-attachments/assets/94ca9fd5-a9e4-46d6-8dd7-a0cd820abaaf)

![Screenshot 2024-12-19 224107](https://github.com/user-attachments/assets/e13c6e96-1fb6-4da0-8b71-c8417fafa2ea)

# Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.
