import autogen
from autogen import GroupChat
from autogen import GroupChatManager

config_list_codellama = [

    {
        "base_url": "http://localhost:8000",
        "model": "ollama/codellama",
        "api_key": "NULL"
    }

]

config_list_mistral = [
    {
        "base_url": "http://localhost:4510",
        "model": "ollama/mistral",
        "api_key": "NULL"
    }
]

chinese = autogen.AssistantAgent("chinese", llm_config={"config_list": config_list_mistral},
                                 system_message="你是一个知识渊博的中国人，你要向大家介绍中国文化",
                                 max_consecutive_auto_reply=1)
american = autogen.AssistantAgent("american", llm_config={"config_list": config_list_mistral},
                                  system_message="你是一个知识渊博的美国人，你要向大家介绍美国文化",
                                  max_consecutive_auto_reply=1)
korea = autogen.AssistantAgent("korea", llm_config={"config_list": config_list_mistral},
                               system_message="你是一个知识渊博的韩国人，你要向大家介绍韩国文化",
                               max_consecutive_auto_reply=1)
host = autogen.UserProxyAgent("host", llm_config={"config_list": config_list_mistral},
                              code_execution_config={"work_dir": "coding", "use_docker": False})

group_chat = GroupChat(
    agents=[chinese, american, korea],
    speaker_selection_method="random",
    messages=[],
    max_round=5,
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list": config_list_mistral},
)
chat_result = host.initiate_chat(
    group_chat_manager,
    message="请你们分别介绍一下你们国家的文化",
    summary_method="reflection_with_llm"
)
print(chat_result)

# chat_result=host.initiate_chats(chinese,message="请你们各自介绍一下你们国家的文化",max_turns=2)
