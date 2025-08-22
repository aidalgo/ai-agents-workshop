# AI Agents Workshop

A comprehensive hands-on workshop for building AI agents using Microsoft's Semantic Kernel, Azure AI services, and Model Context Protocol (MCP). This workshop takes you through a progressive journey from basic agent concepts to advanced multi-agent systems and metacognitive agents.

## 🎯 Workshop Overview

This workshop provides practical experience in building AI agents across multiple frameworks and platforms. You'll learn to create intelligent agents that can use tools, perform RAG (Retrieval-Augmented Generation), plan and execute complex tasks, and work collaboratively in multi-agent systems.

## 📚 Workshop Modules

### 00. Workshop Setup
- Environment configuration
- Azure AI Foundry setup
- Authentication and credentials
- Required dependencies

### 01. Introduction to AI Agents
- Understanding AI agent fundamentals
- Basic agent creation with Semantic Kernel
- Agent communication patterns

### 02. Tool Use
- Creating and using custom tools
- Function calling capabilities
- Tool integration patterns

### 03. Agentic RAG
- Retrieval-Augmented Generation with agents
- ChromaDB integration
- Document search and retrieval

### 04. System Message Framework
- Advanced prompting techniques
- System message design patterns
- Context management

### 05. Planning & Design
- Agent planning capabilities
- Task decomposition
- Strategic thinking patterns

### 06. Multi-Agent Systems
- Agent-to-agent communication
- Collaborative workflows
- Coordination patterns

### 07. Metacognition
- Self-reflective agents
- Learning and adaptation
- Performance monitoring

### 08. Microsoft Learn MCP Integration
- Using pre-built MCP tools
- Microsoft Learn integration
- Standard MCP patterns

### 09. Custom MCP Tools
- Building custom MCP servers
- Inventory management example
- Custom tool development

## 🚀 Getting Started

### Prerequisites

- **Python 3.12+** (Required)
- **Azure Subscription** (For Azure AI services)
- **VS Code** (Recommended IDE)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/aidalgo/ai-agents-workshop.git
cd ai-agents-workshop
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
```

5. **Configure your `.env` file with your credentials** (see setup guide below)

## ⚙️ Environment Setup

### Required Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_API_VERSION=2025-01-01-preview

# Azure AI Project Configuration
AZURE_SUBSCRIPTION_ID=your_subscription_id
AZURE_AI_PROJECT_NAME=your_project_name
AZURE_OPENAI_SERVICE=your_openai_service_name
AZURE_OPENAI_RESOURCE_GROUP=your_resource_group

# For RAG Examples (Optional)
AZURE_SEARCH_SERVICE_ENDPOINT=your_search_endpoint
AZURE_SEARCH_API_KEY=your_search_api_key

# Additional Deployments
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=text-embedding-ada-002
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o
```

### Authentication Setup

This workshop uses **keyless authentication** with Azure AD for enhanced security:

1. **Sign in to Azure:**
```bash
az login --use-device-code
```

2. **Select your subscription:**
```bash
az account set --subscription "Your Subscription Name"
```

## 🏗️ Architecture

The workshop demonstrates three main agent architectures:

1. **Semantic Kernel Agents** - Microsoft's native agent framework
2. **AutoGen Framework** - Multi-agent conversation framework  
3. **Azure AI Agent Service** - Cloud-based agent service

## 🛠️ Technologies Used

- **[Semantic Kernel](https://github.com/microsoft/semantic-kernel)** - Microsoft's agent framework
- **[Azure OpenAI](https://azure.microsoft.com/products/ai-services/openai-service)** - GPT models and embeddings
- **[Azure AI Foundry](https://azure.microsoft.com/products/ai-foundry)** - AI development platform
- **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)** - Tool integration standard
- **[ChromaDB](https://www.trychroma.com/)** - Vector database for RAG
- **[Azure AI Search](https://azure.microsoft.com/products/ai-services/ai-search)** - Enterprise search service

## 📁 Project Structure

```
ai-agents-workshop/
├── 00-workshop-setup/          # Setup instructions and configuration
├── 01-intro-to-ai-agents/      # Basic agent concepts
├── 02-tool-use/                # Tool integration examples
├── 03-agentic-rag/            # RAG implementation with agents
├── 04-system-message-framework/ # Advanced prompting
├── 05-planning-design/         # Agent planning capabilities
├── 06-multi-agent/            # Multi-agent systems
├── 07-metacognition/          # Self-reflective agents
├── 08-use-agent-tools-with-mslearn-mcp/ # Microsoft Learn MCP
├── 09-use-agent-tools-with-custom-mcp/  # Custom MCP tools
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
└── README.md                 # This file
```

## 🚀 Running the Notebooks

Each module contains Jupyter notebooks that you can run step-by-step:

1. **Open VS Code** and ensure you're using Python 3.12+
2. **Navigate** to any module directory
3. **Open** the `.ipynb` files
4. **Run** cells sequentially to follow the examples

### Example: Running the Custom MCP Agent

```bash
cd 09-use-agent-tools-with-custom-mcp
# Start the MCP server (in one terminal)
python server.py

# Run the notebook (in VS Code or Jupyter)
# Open 09-custom-mcp-agent.ipynb
```

## 🎓 Learning Objectives

By completing this workshop, you will:

- ✅ Understand AI agent architecture and design patterns
- ✅ Build agents with tool-calling capabilities
- ✅ Implement RAG systems with vector databases
- ✅ Create multi-agent collaborative systems
- ✅ Develop custom MCP tools and servers
- ✅ Apply metacognitive patterns for agent improvement
- ✅ Deploy agents using Azure AI services

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## 🆘 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/aidalgo/ai-agents-workshop/issues)
- **Documentation**: Detailed setup instructions in [`00-workshop-setup/README.md`](00-workshop-setup/README.md)
- **Community**: Join discussions in the repository discussions section

## 🏷️ Tags

`ai-agents` `semantic-kernel` `azure-ai` `mcp` `rag` `multi-agent` `metacognition` `python` `jupyter` `workshop`

---

**Happy learning!** 🎉 Start with module 00 for detailed setup instructions, then progress through the modules at your own pace.
