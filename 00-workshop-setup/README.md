# Course Setup

## Introduction

This lesson will cover how to run the code samples of this workshop.

## Clone or Fork this Repo

To begin, please clone or fork the GitHub Repository. This will make your own version of the course material so that you can run, test, and tweak the code!

This can be done by clicking the link to <a href="https://github.com/aidalgo/ai-agents-workshop/fork" target="_blank">fork the repo</a>

Or just clone to you local repository: 

HTTPS
```bash
git clone https://github.com/aidalgo/ai-agents-workshop.git
```

After cloning:

```bash
cd ai-agents-workshop
ls -la
```

## Running the Code

This course offers a series of Jupyter Notebooks that you can run to get hands-on experience building AI Agents using the **Semantic Kernel Framework** with **Azure OpenAI**.

### Workshop Lessons

The workshop includes the following lessons:

1. **01-intro-to-ai-agents** - Introduction to Semantic Kernel and basic agent creation
2. **02-tool-use** - Using tools and function calling with agents
3. **03-agentic-rag** - Retrieval-Augmented Generation with ChromaDB
4. **04-system-message-framework** - System message frameworks and agent instructions
5. **05-planning-design** - Agent planning and design patterns
6. **06-multi-agent** - Multi-agent systems and coordination
7. **07-metacognition** - Agent metacognition and self-reflection
8. **08-use-agent-tools-with-mslearn-mcp** - Using Microsoft Learn documentation via MCP
9. **09-use-agent-tools-with-custom-mcp** - Creating custom MCP servers

All examples use **Azure OpenAI Service** for the language models and **Semantic Kernel** as the AI agent framework.

## Requirements

- Python 3.12+
  - **NOTE**: If you don't have Python3.12 installed, ensure you install it. Then create your venv using python3.12 to ensure the correct versions are installed from the requirements.txt file.
- Azure Subscription - For Access to Azure OpenAI Service
- Azure OpenAI Service - For Language Model Access

We have included a `requirements.txt` file in the root of this repository that contains all the required Python packages to run the code samples.

You can install them by running the following command in your terminal at the root of the repository:

```bash
pip install -r requirements.txt
```

We recommend creating a Python virtual environment to avoid any conflicts and issues.

## Setup VSCode

Make sure that you are using the right version of Python in VSCode.

![image](./images/python-in-vscode.png)

## Azure OpenAI Service Setup

To run the notebooks in this workshop, you'll need to set up Azure OpenAI Service:

- Create an Azure OpenAI resource in the Azure portal
- Deploy a GPT-4o or GPT-4o-mini model
- Note your endpoint and deployment name
- Get your API key for authentication

## Environment Configuration

### Create Your `.env` File

To create your `.env` file run the following command in your terminal at the root of the repository:

```bash
cp .env.example .env
```

This will copy the example file and create a `.env` in your directory where you can fill in the values for the environment variables.

### Required Environment Variables

Open the `.env` file in your favorite text editor and fill in these required values:

```bash
# Azure OpenAI settings (Required for all notebooks)
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
```

### Optional: Azure AD Authentication

As a security best practice, you can use [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) to authenticate to Azure OpenAI with Microsoft Entra ID.

To use Azure AD authentication:

1. Open a terminal and run `az login --use-device-code` to sign in to your Azure account
2. Select your subscription in the terminal
3. Comment out the `AZURE_OPENAI_API_KEY` line in your `.env` file
4. The notebooks will automatically use Azure AD authentication

### Additional Setup for Specific Lessons

#### Lesson 03 - Agentic RAG with ChromaDB

This lesson uses ChromaDB for vector storage. If you encounter SQLite version issues:

```bash
pip install pysqlite3-binary
```

And add this code at the start of the notebook:

```python
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
```

#### Lessons 08-09 - MCP (Model Context Protocol)

These lessons demonstrate connecting to external tools via MCP. No additional setup is required as they use HTTP-based MCP servers.

## Python Virtual Environment Setup

We strongly recommend creating a Python virtual environment:

```bash
# Create virtual environment
python3.12 -m venv ai-agents-env

# Activate virtual environment
# On macOS/Linux:
source ai-agents-env/bin/activate
# On Windows:
ai-agents-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Getting Started

Once you have completed the setup:

1. Navigate to the lesson you want to start with (e.g., `01-intro-to-ai-agents/notebook/`)
2. Open the Jupyter notebook in VS Code
3. Select your Python environment/kernel
4. Run the cells to start building AI agents!

Each lesson builds upon the previous one, so we recommend starting with lesson 01 and working through them sequentially.
