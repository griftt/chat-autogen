# import  ollama
# rsp=ollama.chat(
#     model="mistral",
#     messages=[{"role":"user","content":"who are you"}],
#     stream=True
#
# )
#
# for chunk in rsp:
#     print(chunk["message"]["content"],end="",flush=True)
# from langchain_community.llms import Ollama
# llm = Ollama(model="mistral")
# llm.invoke("how can langsmith help with testing?")
import nltk
nltk.download('punkt', force=True)