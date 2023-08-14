import os

from langchain.chat_models import ChatOpenAI

# !LLMS tutorial
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
chat_model = ChatOpenAI()

print("\033[41mLLMs First Prompts\033[0m")
print("----- LLM -----")
print(llm.predict("こんにちは"))
print()

print("----- Chat Model -----")
print(chat_model.predict("こんにちは"))
print()

print("\033[42mString変数を与えた場合\033[0m")
text = "カラフルな靴下を作成する会社にふさわしい名前を5つ教えてください"
print(f"{text=}")

print("----- LLM -----")
print(llm.predict(text))
print()

print("----- Chat Model -----")
print(chat_model.predict(text))
print()
