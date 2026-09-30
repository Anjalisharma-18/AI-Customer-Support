# AI Customer Support & Ticket Automation System

## Overview

An AI-powered customer support system built with Python and FastAPI.

## Features

- Customer support chat
- Order status
- Payment status
- Delivery status
- Support ticket creation
- Human escalation
- Conversation memory
- Intent detection
- RAG and knowledge-base search
- ChromaDB vector database
- SQLite database
- Web frontend

## Technology

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Sentence Transformers
- ChromaDB
- HTML, CSS, JavaScript
- Pytest

## API

- POST `/chat`
- POST `/tickets`
- GET `/tickets/{ticket_id}`
- GET `/orders/{order_id}`
- GET `/payments/{order_id}`
- POST `/escalate`

## Testing

Run:

`python -m pytest .\tests -v`

Current result: **8 tests passed.**

## Project Status

Core backend, database, RAG, tools, memory, APIs, tests, and frontend are implemented.

LLM API integration and final documentation/demo preparation remain.