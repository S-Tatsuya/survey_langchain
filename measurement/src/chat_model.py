from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI()


def messages_in_message_out():
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


if __name__ == "__main__":
    messages_in_message_out()
