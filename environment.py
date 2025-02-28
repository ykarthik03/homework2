# environment.py
import os
from dotenv import load_dotenv

# Load environment variables from .env if it exists
load_dotenv()

# Configuration variables with defaults
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DATABASE_USER = os.getenv("DATABASE_USER", "ROOT")
