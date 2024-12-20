# Chat With PDF

This project enables interaction with PDF documents using AI-powered question-answering. The app extracts text, tables, and images from uploaded PDFs, processes the data, and allows users to ask questions about the content.

## Features

- **PDF Text Extraction**: Extracts plain text, tables, and performs OCR on images/graphs from PDFs.
- **AI Question-Answering**: Uses a large language model (LLM) to answer questions based on PDF content.
- **Vector Store**: Embeds PDF text into a searchable FAISS index for efficient information retrieval.
- **Streamlit UI**: User-friendly interface for uploading files and interacting with the app.

## Requirements

To run this project, install the following Python libraries:
- `pdfplumber`
- `PyMuPDF`
- `streamlit`
- `langchain`
- `pytesseract`
- `Pillow`

## How to Run
Start the Streamlit application:

streamlit run app.py

Open the app in your browser at http://localhost:8501.

Upload your PDF files using the sidebar.

Click the "Process PDFs" button to analyze the content.

Ask questions in the input box, and the app will respond with answers based on the uploaded PDF content.

## Key Files
app.py: The main script containing the Streamlit app and processing logic.
faiss_store_openai.pkl: Pickle file storing the FAISS vector index for retrieved embeddings.

## Functionality Breakdown

#Text Extraction
Extracts plain text, tables, and image-based text from uploaded PDFs.

# OCR Processing
Uses PyMuPDF and Tesseract to analyze embedded images like graphs and pie charts.

# Vector Embedding
Splits text into manageable chunks and generates embeddings using sentence-transformers.

# Retrieval-based QA
Employs LangChain's RetrievalQA to retrieve and answer questions using a pre-built vector index.

## Example Usage
Upload a PDF with financial statements.
Ask, "What are the revenue figures for 2023?"
Get an AI-generated answer derived from tables, text, or graphs in the document.
Future Enhancements
Add support for multi-language OCR.
Improve table parsing accuracy.
Deploy the app on cloud platforms like AWS or Streamlit Sharing.

![Screenshot 2024-12-19 220752](https://github.com/user-attachments/assets/9738d17e-ea08-4aba-98eb-37ef27aa9bf9)

![Screenshot 2024-12-19 220853](https://github.com/user-attachments/assets/d5248a97-45f4-4472-8611-d56671400557)

![Screenshot 2024-12-19 221007](https://github.com/user-attachments/assets/7851326a-6bf9-4df6-89b7-bd016f46add1)

![Screenshot 2024-12-19 221909](https://github.com/user-attachments/assets/0d530cee-dc80-4b65-b4ba-26f737f11e54)


## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.





