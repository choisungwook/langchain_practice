
from langchain.llms import CTransformers
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from langchain.prompts import (
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.chains import LLMChain


def getModel():
    return CTransformers(model="llama-2-7b-chat.Q5_K_M.gguf")


def generatePrompt():
    template_messages = [
        SystemMessage(content="You are a helpful assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]

    return ChatPromptTemplate.from_messages(template_messages)


model = getModel()
prompt_template = generatePrompt()
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

chain = LLMChain(llm=model, prompt=prompt_template, memory=memory)

print(
    chain.run(
        text="What can I see in Vienna? Propose a few locations. Names only, no details."
    )
)
