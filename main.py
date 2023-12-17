from typing import List

from langchain.llms import CTransformers
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser


class CommaSeparatedListOutputParser(BaseOutputParser[List[str]]):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str) -> List[str]:
        """Parse the output of an LLM call."""
        return text.strip().split(", ")


model = CTransformers(model="llama-2-7b-chat.Q5_K_M.gguf")

template = "You are a helpful assistant that translates English to Korean."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("human", human_template),
    ]
)

chain = chat_prompt | model | CommaSeparatedListOutputParser()
outputs = chain.invoke({"text": "Apple"})

for output in outputs:
    print(output)
