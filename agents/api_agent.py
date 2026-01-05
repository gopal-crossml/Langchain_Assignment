from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from cred import gemini_api_key
from tools.weather import get_weather
from .multi_tools import llm
from prompts import system_prompt

api_agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt=system_prompt
)