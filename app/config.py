import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    # Aap model badal sakte hain, jaise "openai/gpt-3.5-turbo" ya "google/gemini-pro"
    MODEL_NAME = "openrouter/auto"