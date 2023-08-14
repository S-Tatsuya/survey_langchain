import os

from langchain.chat_models import ChatOpenAI

# !LLMS tutorial
from langchain.llms import OpenAI
from langchain.schema import HumanMessage

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
chat_model = ChatOpenAI()

print("\033[41mLLMs First Prompts: predict\033[0m")
print("----- LLM -----")
print(llm.predict("こんにちは"))
print()

print("----- Chat Model -----")
print(chat_model.predict("こんにちは"))
print()

print("\033[42mString変数を与えた場合: predict\033[0m")
text = "カラフルな靴下を作成する会社にふさわしい名前を5つ教えてください"
print(f"{text=}")

print("----- LLM -----")
print(llm.predict(text))
print()

print("----- Chat Model -----")
print(chat_model.predict(text))
print()

print("\033[43m配列を与えることのできるメソッド: predict_messages\033[0m")
text = "カラフルな靴下を作成する会社にふさわしい名前を5つ教えてください"
print(f"{text=}")
messages = [HumanMessage(content=text)]
print(f"Human Message={messages}")

print("----- LLM -----")
print(llm.predict_messages(messages))
print()

print("----- Chat Model -----")
print(chat_model.predict_messages(messages))
print()
