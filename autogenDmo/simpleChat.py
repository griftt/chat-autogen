import autogen
from autogen import ChatResult

config_list_codellama=[

    {
        "base_url":"http://localhost:8000",
        "model":"ollama/codellama",
        "api_key":"NULL"
    }

]

config_list_mistral=[
    {
        "base_url":"http://localhost:8000",
        "model":"ollama/mistral",
        "api_key":"NULL"
    }
]




def initSimeDoubleChat(message)-> ChatResult:
    chinese = autogen.AssistantAgent("chinese", llm_config={"config_list": config_list_mistral},
                                     system_message="你是一个知识渊博的中国人，你要向大家介绍中国文化",
                                     max_consecutive_auto_reply=1)
    american = autogen.AssistantAgent("", llm_config={"config_list": config_list_mistral},
                                      system_message="你是一个知识渊博的美国人，你要向大家介绍美国文化",
                                      max_consecutive_auto_reply=1)
    korea = autogen.AssistantAgent("chinese", llm_config={"config_list": config_list_mistral},
                                   system_message="你是一个知识渊博的韩国人，你要向大家介绍韩国文化",
                                   max_consecutive_auto_reply=1)

    host = autogen.UserProxyAgent("host", llm_config={"config_list": config_list_mistral},
                                  code_execution_config={"work_dir": "coding", "use_docker": False})

    return host.initiate_chat(chinese, message=message, max_turns=2)




