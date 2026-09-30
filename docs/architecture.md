# System Architecture

```text
Customer
   |
   v
Frontend (HTML/CSS/JavaScript)
   |
   v
FastAPI Backend
   |
   +------------------+
   |                  |
   v                  v
Intent Detection     Conversation Memory
   |                  |
   v                  v
AI Agent ---------> Decision
   |
   +--------------------+--------------------+
   |                    |                    |
   v                    v                    v
RAG / Knowledge Base  Database Tools    Human Escalation
   |                    |                    |
   v                    v                    v
Embeddings           Orders/Payments     Support Team
   |
   v
ChromaDB
   |
   v
Grounded Response
   |
   v
Customer