from langchain.llms import OpenAI

llm = OpenAI()


def llm_string_in_string_out():
    print(llm("Tell me a joke"))


if __name__ == "__main__":
    llm_string_in_string_out()
