import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app


_ = load_dotenv()
logging.basicConfig(level=logging.INFO)

app: FastAPI = get_fast_api_app(
    agents_dir="./app/agents",
    session_service_uri="sqlite:///default.db",
    allow_origins=["*"],
    web=True,
)
