import pdfplumber
from docx import Document
from transformers import pipeline

# Initialize the summarizer pipeline from Hugging Face
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
pdf_path = "D:/sami work/file downloading.pdf.pdf"
# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

# Function to extract text from a Word document (DOCX)
def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from DOCX: {e}")
        return None

# Function to summarize the extracted text
def summarize_text(text):
    try:
        # Generate the summary using the pre-trained BART model
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Sorry, I couldn't summarize the document."

# Main chatbot function to interact with the user
def chatbot():
    print("Hi! I'm your document summarizer bot. Please upload a document (PDF or DOCX).")
    
    while True:
        file_path = input("Enter the file path (or 'exit' to quit): ")
        if file_path.lower() == "exit":
            print("Goodbye!")
            break
        
        # Check for the file format and extract text accordingly
        if file_path.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            print("Unsupported file format. Please upload a PDF or DOCX file.")
            continue
        
        if text:
            print("Extracting and summarizing text...")
            # Check if the text is empty
            if len(text.strip()) == 0:
                print("The document is empty or unreadable.")
            else:
                # Summarize the extracted text
                summary = summarize_text(text)
                print("Summary:\n", summary)
        else:
            print("An error occurred while processing the document. Please try again.")

# Run the chatbot
