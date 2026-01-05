"""
Agent that intelligently selects ONE tool.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from cred import gemini_api_key
from tools.math import math_calculator
from tools.text_analyzer import analyze_text
from tools.date import future_date

# chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=gemini_api_key,
    temperature=0
)

tools = [math_calculator, analyze_text, future_date]

# agent creation
agent = create_agent(
    model=llm,
    tools=tools
)
