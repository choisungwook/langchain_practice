from typing import List

from langchain.llms import CTransformers
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

llm = CTransformers(model="llama-2-7b-chat.Q5_K_M.gguf")

print(llm("AI is going to"))
