# 🌿 Eco-CSR AI Consultant | RAG-Powered Autonomous Agent

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pinecone)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google)

---

## 📖 Project Description

**Eco-CSR AI Consultant** is an enterprise-grade autonomous AI application built to help businesses align sustainability with profitability.

Instead of acting as a generic chatbot, this system uses a specialized **Retrieval-Augmented Generation (RAG)** architecture that processes:

- Corporate sustainability reports
- Financial documents
- Decarbonization case studies
- Internal knowledge bases

The agent generates actionable sustainability strategies to:

✅ Reduce operational costs  
✅ Optimize resource utilization  
✅ Improve ESG alignment  
✅ Support sustainable revenue growth

The system grounds all responses using local vector databases to minimize hallucinations and ensure factual outputs.

---

## 🎥 Agent in Action

![Eco-CSR Agent Demo](demo.gif)

---

## ✨ Key Features

### 🔹 High-Dimensional Vector Ingestion
Uses **Gemini Embeddings (3072 dimensions)** with **Pinecone Serverless** for semantic retrieval.

### 🔹 Stateful Multi-Turn Memory
Built using:

- LangGraph state machines
- SQLite persistence
- `checkpoints.db`

Maintains conversation history across enterprise sessions.

### 🔹 Production Resilience
Includes:

- Rate limiting protection
- Exponential retry workflows
- API stability handling

### 🔹 Executive UI Experience
Custom corporate dashboard using Streamlit with CSS styling.

---

## 🛠 Tech Stack

### Frameworks
- LangChain
- LangGraph Core

### LLM & Embeddings
- Google Gemini 2.5 Flash
- Gemini Embeddings (MRL Optimized)

### Vector Store
- Pinecone Serverless Database

### State Management
- SQLite Checkpointer Runtime

### Frontend
- Streamlit
- Custom CSS
- HTML Injection

---

# 🚀 Local Installation Guide

## Prerequisites

Install:

- Python 3.11+

---

## 1️⃣ Clone Repository

```bash
git clone https://github.com/iAmirJ/eco-csr-agent.git
cd eco-csr-agent
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env`

```env
GOOGLE_API_KEY=your_google_key
PINECONE_API_KEY=your_pinecone_key
```

---

## 5️⃣ Run Data Ingestion

Place PDFs or sustainability reports inside project directory.

Run:

```bash
python ingest.py
```

Wait for successful ingestion confirmation.

---

## 6️⃣ Launch Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 💼 Custom AI Development Services

**Aamir Javed**  
Graduate AI & Full-Stack Engineer

Specialized in:

- Enterprise RAG Systems
- Autonomous Agents
- LLM Applications
- AI Workflow Automation
- Knowledge Base Assistants

### Contact

📞 WhatsApp: +92 305 1925331

🏢 Agency: Kodelix

📫 Available for freelance and enterprise projects

---

### ⭐ If you like this project, give it a star.