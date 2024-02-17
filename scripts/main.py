import os
from dotenv import load_dotenv
import openai
import langchain_community
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.agents import AgentType

import pprint
from langchain.agents import get_all_tool_names, load_tools, initialize_agent 
from langchain.agents import AgentType


class APIKeys:
    def __init__(self):
        load_dotenv()  # loads the environment variables
        self.openai_api_key = os.environ.get("OPENAI_API_KEY")
        self.huggingfacehub_api_key = os.environ.get("HUGGINGFACEHUB_API_KEY")
        self.serpapi_api_key = os.environ.get("SERPAPI_API_KEY")

        if self.huggingfacehub_api_key is None:
            raise ValueError("HUGGINGFACE_API_KEY is not set in the environment.")

    def set_openai_api_key(self):
        openai.api_key = self.openai_api_key

# Usage
api_keys = APIKeys()
api_keys.set_openai_api_key()