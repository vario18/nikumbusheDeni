import logging

from fastapi import FastAPI
from .model import create_db_and_tables

app = FastAPI()

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# STARTUP


@app.on_event("startup")
async def startup():
    """
    Creates database and tables on startup
    """
    logging.info("Startup")
    logging.info("Creating database and tables")
    create_db_and_tables()


@app.get("/")
def home():
    return "Server running"
