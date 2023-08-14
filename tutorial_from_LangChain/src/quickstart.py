import os

from langchain.chat_models import ChatOpenAI

# !LLMS tutorial
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
chat_model = ChatOpenAI()

print("----- LLM -----")
print(llm.predict("こんにちは"))
print()

print("----- Chat Model -----")
print(chat_model.predict("こんにちは"))
