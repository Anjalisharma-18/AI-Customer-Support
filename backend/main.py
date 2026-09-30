import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import Base, engine
from backend.models.order import Order
from backend.models.payment import Payment
from backend.models.ticket import Ticket
from backend.models.conversation import Conversation
from backend.api.chat import router as chat_router
from backend.api.orders import router as orders_router
from backend.api.payments import router as payments_router
from backend.api.tickets import router as tickets_router
from backend.api.escalation import router as escalation_router


# Application logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Customer Support & Ticket Automation System"
)


# Allow frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Connect Chat API
app.include_router(chat_router)

# Connect Orders API
app.include_router(orders_router)

# Connect Payments API
app.include_router(payments_router)

# Connect Tickets API
app.include_router(tickets_router)

# Connect Escalation API
app.include_router(escalation_router)


@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "message": "AI Customer Support & Ticket Automation System is running"
    }


@app.get("/health")
def health():
    logger.info("Health check accessed")

    return {
        "status": "healthy",
        "service": "AI Customer Support & Ticket Automation System"
    }