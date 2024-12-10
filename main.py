from llama_index.readers.file import PDFReader
from pathlib import Path
from llama_index.llms.azure_openai import AzureOpenAI
from dotenv import load_dotenv
import os
import json
from models import Invoice

# Load environment variables
load_dotenv()

# Store environment variables
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
model = os.getenv("AZURE_OPENAI_MODEL")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Print environment variables (masking API key)
print("Azure OpenAI Configuration:")
print(f"Deployment: {deployment}")
print(f"Model: {model}")
print(f"API Key: {'*' * 8}{api_key[-4:] if api_key else 'Not Set'}")
print(f"API Version: {api_version}")
print(f"Endpoint: {endpoint}")

# Initialize Azure OpenAI
llm = AzureOpenAI(
    engine=deployment,
    model=model,
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint
)

# Read PDF
pdf_reader = PDFReader()
documents = pdf_reader.load_data(file=Path("/home/azureuser/repos/struct-invoice/data/my-invoice.pdf"))
text = documents[0].text
print("\nPDF Content:")
print(text)

sllm = llm.as_structured_llm(Invoice)

response = sllm.complete(text)

json_response = json.loads(response.text)
print(json.dumps(json_response, indent=2))