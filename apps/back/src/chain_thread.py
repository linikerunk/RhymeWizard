from langchain.callbacks.base import BaseCallbackManager
from src.thread_generator import ThreadedGenerator
from src.chain_stream_handler import ChainStreamHandler
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
import os


def chain_thread(generator: ThreadedGenerator, template: str, prompt: str) -> None:
    try:
        system_message_prompt = SystemMessagePromptTemplate.from_template(
            template)
        human_template = "{text}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(
            human_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt])
        chain = LLMChain(
            llm=ChatOpenAI(
                streaming=True,
                temperature=0.9,
                callback_manager=BaseCallbackManager(
                    [ChainStreamHandler(generator)]),
                openai_api_key=os.getenv("OPENAI_API_KEY")
            ),
            prompt=chat_prompt,
        )

        chain.run(prompt)
    finally:
        generator.close()
