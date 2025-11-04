from dotenv import load_dotenv
import os


load_dotenv()


BASE_URL = os.getenv("BASE_URL")
MONGO_URI = os.getenv("MONGO_URI")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
