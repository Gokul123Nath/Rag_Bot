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
model_name = "bigscience/bloom-1b7" # Other open sourced like EleutherAI/gpt-j-6B, bigscience/bloom-1b7, facebook/opt-1.3b can be used
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_text_replacement(prompt, max_length=1000):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_length=max_length)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def generate_text(data : str, max_length : int = 1000) -> str:
    """
    Generates text based on the provided prompt using an API.

    Args:
        prompt (str): The input text based on which the text will be generated.
        max_length (int, optional): The maximum length of the generated text. Defaults to 1000.

    Returns:
        str: The generated text if the request is successful.
             An error message if the request fails or the response can't be parsed as JSON.
    """
    payload = {
        "inputs": f"""
        Task:
        Using the context provided, generate a detailed and coherent response that addresses the following data:
        {data}

        Guidelines:
        - Ensure the response is well-structured and logically organized.
        - Use appropriate language and tone based on the context.
        - Include relevant examples or details from the provided context to support the response.
        - Maintain clarity and conciseness in the explanation.""",
        "parameters": {"max_length": max_length, "temperature": 0.7},
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    try:
        response_json = response.json()
        if response.status_code == 200:
            return response_json[0]["generated_text"]
        else:
            return f"Error: {response_json}"
    except ValueError: 
        return f"Error: Unable to parse JSON. Raw response content: {response.text}"
    

