import dotenv
dotenv.load_dotenv()

from langchain.schema import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

chat = ChatOpenAI()
chat.invoke(
    [
        HumanMessage(
            content="Translate this sentence from English to French: I love programming."
        )
    ]
)