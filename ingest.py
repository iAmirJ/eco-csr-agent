import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# 1. Environment variables load karo (.env file se)
load_dotenv()

print("🚀 Data Ingestion Process Started...")

# 2. PDF Load Karna
# Apni PDF file ko project folder mein rakho aur uska naam yahan update karo
file_path = "climate-decarbonization-stewardship-summary.pdf"  # <-- YAHAN APNI FILE KA NAAM LIKHO

try:
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"📄 Document loaded: {len(documents)} pages found.")
except Exception as e:
    print(f"⚠️ Error loading document: {e}")
    print("Make sure file ka naam sahi hai aur woh project folder mein mojood hai.")
    exit()

# 3. Text ko chotay hisson (chunks) mein todna (Taake AI asani se search kar sake)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)
print(f"✂️ Text split into {len(chunks)} chunks.")

# 4. Embeddings Setup (Wahi model jo humne backend.py mein lagaya hai)
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# 5. Pinecone mein Embeddings upload karna
index_name = "csr-agent-index"
print(f"⬆️ Uploading data to Pinecone index: '{index_name}'...")

try:
    PineconeVectorStore.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        index_name=index_name,
        pinecone_api_key=os.getenv("PINECONE_API_KEY")
    )
    print("✅ Data successfully uploaded to Pinecone!")
except Exception as e:
    print(f"⚠️ Error uploading to Pinecone: {e}")