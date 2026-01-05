**LangChain Assignment 🚀
**
This project demonstrates the creation and usage of custom tools and agents using LangChain.
It is structured to show single-tool agents, multi-tool agents, and custom utility tools such as math evaluation, text analysis, date handling, and weather lookup.

**🎯 Objectives**
- Understand LangChain custom tools
- Build single-tool and multi-tool agents
- Safely evaluate user input (math, text)
- Organize code using clean modular architecture
- Practice agent-tool orchestration

**🛠️ Technologies Used**
- Python 3.10+
- LangChain
- GenAI / LLM APIs
- dotenv

AST (for safe math evaluation)

**⚙️ Setup Instructions**
1️⃣ Clone the Repository
git clone <repository-url>
cd LANGCHAIN_ASSIGNMENT

**2️⃣ Create Virtual Environment**
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

**3️⃣ Install Dependencies**
pip install -r requirements.txt

**4️⃣ Configure Environment Variables**

Create a .env file:

OPENAI_API_KEY=your_api_key_here

▶️ Running the Project
python main.py
This will initialize the selected agent and execute the assigned tasks using LangChain tools.

🧠 Agents Overview
🔹 Single Tool Agent
- Uses one tool at a time
- Ideal for focused tasks

🔹 Multi Tool Agent
- Chooses between multiple tools dynamically
- Demonstrates LangChain reasoning and routing

🔹 API Agent
- Interacts with external APIs
- Uses credentials securely from .env or cred.py

**🔐 Security Notes**
- API keys are never hard-coded
- .env is included in .gitignore
- Math tool uses AST parsing to prevent unsafe execution

**📌 Learning Outcomes**
- Practical understanding of LangChain architecture
- Safe tool execution techniques
- Agent-based reasoning workflows
- Clean and scalable project structure