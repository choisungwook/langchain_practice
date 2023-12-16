from langchain.llms import CTransformers

llm = CTransformers(model="llama-2-7b-chat.Q5_K_M.gguf")

print(llm("AI is going to"))
