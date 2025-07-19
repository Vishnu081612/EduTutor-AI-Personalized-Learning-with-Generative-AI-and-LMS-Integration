from dotenv import load_dotenv
import os

load_dotenv()

print("DEBUG APIKEY:", os.getenv("WATSONX_APIKEY"))
print("DEBUG URL:", os.getenv("WATSONX_URL"))
print("DEBUG PROJECT_ID:", os.getenv("WATSONX_PROJECT_ID"))
