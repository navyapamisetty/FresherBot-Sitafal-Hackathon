#pip install beautifulsoup4
#pip install requests
#pip install langchain
#pip install streamlit
#pip install faiss-cpu

import requests
import os
from bs4 import BeautifulSoup
import streamlit as st
import pickle
import time
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Streamlit UI
st.title("Chat with Website Content")
st.sidebar.title("Web Scraper")

url = st.sidebar.text_input("Enter Website URL")
scrape_button = st.sidebar.button("Scrape Website")
file_path = "faiss_store_website.pkl"

main_placeholder = st.empty()
llm = ChatGroq(
    temperature=0,
    groq_api_key="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",  # Replace with your actual Groq API key
    model_name="llama-3.1-70b-versatile"
)

# Function to scrape website content
def scrape_website_content(website_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(website_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract visible text
        for script in soup(["script", "style"]):
            script.decompose()  # Remove scripts and styles

        visible_text = soup.get_text()
        lines = (line.strip() for line in visible_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = '\n'.join(chunk for chunk in chunks if chunk)

        return text_content
    
    except Exception as e:
        st.error(f"Error scraping website: {str(e)}")
        return ""

    
    except Exception as e:
        st.error(f"Error scraping website: {str(e)}")
        return ""

if scrape_button:
    if not url:
        st.error("Please enter a valid URL.")
    else:
        st.sidebar.success("Website Content Scraped Successfully")
        website_text = scrape_website_content(url)

        # Split text into chunks for processing
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        text_chunks = text_splitter.split_text(website_text)

        # Create embeddings and vector store
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore_website = FAISS.from_texts(text_chunks, embeddings)

        # Save FAISS index to pickle
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        time.sleep(2)

        # Save the FAISS index to a pickle file for future use
        with open(file_path, "wb") as f:
            pickle.dump(vectorstore_website, f)

# Query input section
query = main_placeholder.text_input("Ask a Question:")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQA.from_llm(llm=llm, retriever=vectorstore.as_retriever())

        # Retrieval-based chain
        retriever = vectorstore.as_retriever()
        chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

        # Get the answer for the query
        result = chain.run(query)

        # Display the answer
        st.header("Answer")
        st.write(result)
