# 🩺 HIA (Health Insights Agent)

AI Agent to analyze health reports and provide detailed medical insights.

## ✅ Overview

**HIA (Health Insights Agent)** is an advanced AI assistant designed to simplify medical report analysis. By leveraging multi-agent LLM architectures and RAG (Retrieval-Augmented Generation), HIA can read blood reports, explain complex medical terms, and provide actionable health insights in simple language.

## 🚀 Key Features

*   **Multi-Agent Intelligence**: 
    *   **Analysis Agent**: Specialized in extracting and interpreting biomarkers from lab reports.
    *   **Chat Agent**: RAG-powered Q&A to answer follow-up questions about your specific results.
*   **Intelligent Model Cascading**: Automatically falls back to cheaper/faster models if primary models are near rate limits, ensuring continuous availability.
*   **Flexible Inputs**:
    *   **PDF Extraction**: Automated text extraction from medical PDF files.
    *   **Manual Fallback**: Support for manual text pasting for scanned or image-based documents.
*   **Session Management**: Persistent history using Supabase, allowing you to return to past analyses at any time.
*   **Daily Analysis Limit**: Built-in quota management (default 15/day) to manage API costs.

## 🛠️ Tech Stack

*   **Framework**: Streamlit (Python)
*   **LLM Provider**: Groq (Llama 3.x models)
*   **Database**: Supabase (PostgreSQL & Auth)
*   **RAG Engine**: LangChain, FAISS, HuggingFace Embeddings
*   **PDF Processing**: pdfplumber

## 📦 Installation & Setup

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/mohabasumeih-sys/Health-Agent.git
    cd Health-Agent
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Credentials**:
    Create a `.streamlit/secrets.toml` file with your credentials:
    ```toml
    SUPABASE_URL = "your-supabase-url"
    SUPABASE_KEY = "your-supabase-key"
    GROQ_API_KEY = "your-groq-api-key"
    DEV_MODE = true # Optional: Set to true for local testing bypass
    ```

4.  **Run the Application**:
    ```bash
    streamlit run src/main.py
    ```

## 📂 Project Structure

*   `src/auth/`: Authentication and session management logic.
*   `src/services/`: Core AI and data processing services.
*   `src/agents/`: Multi-agent definitions and model management.
*   `src/components/`: Reusable Streamlit UI components.
*   `src/utils/`: PDF extraction and input validation utilities.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
