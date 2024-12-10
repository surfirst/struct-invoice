# 结构化发票处理系统

## 项目简介
这是一个基于 LlamaIndex 和 Azure OpenAI 的智能发票处理系统，能够自动从PDF发票中提取关键信息并将其结构化。系统使用先进的AI技术来识别和解析发票中的各种字段，如供应商信息、金额、税费等。

## 技术框架
- **LlamaIndex**: 用于文档处理和结构化输出
- **Azure OpenAI**: 提供强大的AI语言模型支持
- **Python**: 编程语言 (3.10+)
- **PDFReader**: PDF文档解析工具
- **Pydantic**: 数据验证和序列化

## 主要功能
- PDF发票文件读取
- 自动提取发票关键信息
- 结构化数据输出（JSON格式）
- 支持的字段包括：
  - 发票编号
  - 发票日期
  - 总金额
  - 供应商信息
  - 商品明细
  - 税额

## 安装说明
1. 克隆项目仓库
```bash
git clone [repository-url]
cd struct-invoice
```

2. 创建并激活Python虚拟环境
```bash
python -m venv llamaindex-env
source llamaindex-env/bin/activate  # Linux/Mac
```

3. 安装依赖包
```bash
pip install -r requirements.txt
```

4. 配置环境变量
复制 `.env.template` 文件为 `.env` 并填入您的 Azure OpenAI 配置：
```bash
cp .env.template .env
```
需要配置的环境变量：
- AZURE_OPENAI_API_KEY
- AZURE_OPENAI_ENDPOINT
- AZURE_OPENAI_MODEL
- AZURE_OPENAI_DEPLOYMENT
- AZURE_OPENAI_API_VERSION

## 使用方法
1. 准备PDF发票文件，放置在 `data` 目录下
2. 运行程序：
```bash
python main.py
```

## 输出示例
程序将输出JSON格式的结构化数据，包含从发票中提取的所有关键信息。

## 注意事项
- 确保PDF文件清晰可读
- 需要有效的Azure OpenAI API访问权限
- 建议使用虚拟环境运行项目

## 贡献指南
欢迎提交Issue和Pull Request来帮助改进项目。

## 许可证
[许可证类型]