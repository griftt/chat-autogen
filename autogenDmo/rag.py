import os

import autogen
import chromadb
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from IPython import get_ipython
config_list_mistral = [
    {
        "base_url": "http://localhost:8000",
        "model": "ollama/mistral",
        "api_key": "NULL"
    }
]

config_list_codellama = [
    {
        "base_url": "http://localhost:26850",
        "model": "ollama/codellama",
        "api_key": "NULL"
    }
]

assistant = RetrieveAssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",

    llm_config={
        "timeout": 600,
        "cache_seed": 42,
        "config_list": config_list_mistral,
    },
)
# ragproxyagent = RetrieveUserProxyAgent(
#     name="ragproxyagent",
#     human_input_mode="NEVER",
#     max_consecutive_auto_reply=3,
#
#     retrieve_config={
#         "task": "qa",
#         "docs_path": [
#             "D:\\fastApiProject\\autogenDmo\\book\\rag.txt"
#
#         ],
#         "context_max_tokens":2000,
#         "custom_text_types": ["pdf"],
#         "chunk_token_size": 2000,
#         "must_break_at_empty_line":False,
#         "model": config_list_mistral[0]["model"],
#         "client": chromadb.PersistentClient(path="chromadb"),
#         "embedding_model": "C:\\Users\\13612\\.cache\\modelscope\\hub\\Jerry0\\text2vec-base-chinese",
#         "get_or_create": True,  # set to False if you don't want to reuse an existing collection, but you'll need to remove the collection manually
#     },
#     code_execution_config=False,  # set to False if you don't want to execute the code
# )
print(os.path.join(os.path.abspath(""), "..", "website", "docs"))
ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="NEVER",

    max_consecutive_auto_reply=3,
    retrieve_config={
        "task": "qa",
        "docs_path": [
            "D:\\fastApiProject\\autogenDmo\\book\\ragmd.md",


        ],

        "chunk_token_size": 2000,
        "model": config_list_codellama[0]["model"],
        "client": chromadb.PersistentClient(path="chromadb"),
        "embedding_model": "all-mpnet-base-v2",
        "must_break_at_empty_line":False,
        "get_or_create": True,  # set to False if you don't want to reuse an existing collection, but you'll need to remove the collection manually
    },
    code_execution_config=False,  # set to False if you don't want to execute the code
)
assistant.reset()
#ragproxyagent.initiate_chat(assistant, problem="What is the workflow in docGPT?", n_results=2)

# given a problem, we use the ragproxyagent to generate a prompt to be sent to the assistant as the initial message.
# the assistant receives the message and generates a response. The response will be sent back to the ragproxyagent for processing.
# The conversation continues until the termination condition is met, in RetrieveChat, the termination condition when no human-in-loop is no code block detected.
# With human-in-loop, the conversation will continue until the user says "exit".
code_problem = "总结一下文档的内容"
ragproxyagent.initiate_chat(
    assistant, message=ragproxyagent.message_generator, problem=code_problem, search_string="RetrieveChat"
)