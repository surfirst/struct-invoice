from llama_index.readers.file import PDFReader
from pathlib import Path
from llama_index.llms.azure_openai import AzureOpenAI
from dotenv import load_dotenv
import os
import json
from models import Invoice

# 加载环境变量
load_dotenv()

# 存储环境变量
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
model = os.getenv("AZURE_OPENAI_MODEL")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# 打印环境变量配置（隐藏API密钥）
print("Azure OpenAI Configuration:")
print(f"Deployment: {deployment}")
print(f"Model: {model}")
print(f"API Key: {'*' * 8}{api_key[-4:] if api_key else 'Not Set'}")
print(f"API Version: {api_version}")
print(f"Endpoint: {endpoint}")

# 初始化 Azure OpenAI
llm = AzureOpenAI(
    engine=deployment,
    model=model,
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint
)

# 读取PDF文件
pdf_reader = PDFReader()
documents = pdf_reader.load_data(file=Path("/home/azureuser/repos/struct-invoice/data/my-invoice.pdf"))
text = documents[0].text
print("\nPDF Content:")
print(text)

# 创建结构化LLM
sllm = llm.as_structured_llm(Invoice)

# 分析PDF并生成发票的结构化输出
response = sllm.complete(text)

# 将响应解析为JSON格式
json_response = json.loads(response.text)

# 打印JSON响应
print(json.dumps(json_response, indent=2))