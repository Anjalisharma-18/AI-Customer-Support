import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./customer_support.db"
)

LLM_API_KEY = os.getenv("LLM_API_KEY", "")

APP_NAME = "AI Customer Support & Ticket Automation System"