from langchain.chat_models import ChatOpenAI

# from langchain.schema import AIMessage  # AIMessageは応答のメッセージの型
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI()


def messages_in_message_out_without_system_message():
    #  AIMessage(content="J'aime programmer.", additional_kwargs={})
    print(
        chat(
            [
                HumanMessage(
                    content=(
                        "Translate this sentence from English to Japanese: "
                        "I love programming."
                    ),
                ),
            ]
        )
    )


def messages_in_message_out_with_system_message():
    messages = [
        SystemMessage(
            content="You are a helpful assistant that translates English to Japanese."
        ),
        HumanMessage(content="I love programming"),
    ]
    print(chat(messages))


if __name__ == "__main__":
    # messages_in_message_out_without_system_message()
    messages_in_message_out_with_system_message()
