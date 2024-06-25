import logging

# from fastapi import FastAPI
from model import create_db_and_tables

logging.info("Creating database and tables")
create_db_and_tables()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """
#     Creates database and tables on startup
#     """
#     logging.info("Startup")
#     logging.info("Creating database and tables")
#     create_db_and_tables()
#     yield
#     logging.info("Application is shutting down")


# app = FastAPI(lifespan=lifespan)


# # Setup logging
# logging.basicConfig(
#     level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )

# # STARTUP

# # @app.on_event("startup")
# # async def startup():
# #     """
# #     Creates database and tables on startup
# #     """
# #     logging.info("Startup")
# #     logging.info("Creating database and tables")
# #     create_db_and_tables()


# @app.get("/")
# def home():
#     return "Server running"
