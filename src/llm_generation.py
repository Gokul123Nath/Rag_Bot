from transformers import AutoModelForCausalLM, AutoTokenizer
import requests, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

MODEL = "bigscience/bloom-1b7"
# Hugging Face Inference API URL
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"

# Headers with Authorization
headers = {"Authorization": f"Bearer {API_KEY}"}

model_name = "facebook/opt-1.3b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text(prompt, max_length=1000):

    payload = {
        "inputs": prompt,
        "parameters": {"max_length": max_length, "temperature": 0.7},
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    try:
        response_json = response.json()
        if response.status_code == 200:
            return response_json[0]["generated_text"]
        else:
            return f"Error: {response_json}"
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        return f"Error: Unable to parse JSON. Raw response content: {response.text}"
    

