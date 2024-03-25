import autogen
from autogen import AssistantAgent, UserProxyAgent
from autogen import GroupChat
from autogen import GroupChatManager



config_list_codellama=[

    {
        "base_url":"http://localhost:8000",
        "model":"ollama/codellama",
        "api_key":"NULL"
    }

]

config_list_mistral=[
    {
        "base_url":"http://localhost:4510",
        "model":"ollama/mistral",
        "api_key":"NULL"
    }
]
#config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")


assistant = AssistantAgent("assistant", llm_config={"config_list": config_list_codellama})
coder = AssistantAgent("coder", llm_config={"config_list": config_list_codellama})
test = AssistantAgent("test", llm_config={"config_list": config_list_codellama})
assistant.description="aassistant"
coder.description="coder"
test.description="test Man"




user_proxy = UserProxyAgent("user_proxy", llm_config={"config_list": config_list_mistral},
                            code_execution_config={"work_dir": "coding","use_docker": False})


group_chat = GroupChat(
    agents=[assistant, coder,test],
    messages=[],
    max_round=6,
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    system_message="give them a interger number",
    llm_config={"config_list":config_list_mistral},
)
#user_proxy.initiate_chat(assistant, message="")
#现在我们创建一个 GroupChatManager 对象，并提供 GroupChat 对象作为输入。我们还需要指定群组聊天管理器的 llm_config ，以便它可以使用LLM来选择下一个代理（ auto 策略）。
chat_result = user_proxy.initiate_chat(
    group_chat_manager,
    message="每个人告诉我一个数字",
    summary_method="reflection_with_llm",
)
