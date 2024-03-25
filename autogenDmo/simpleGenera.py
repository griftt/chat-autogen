import autogen

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

chinese=autogen.AssistantAgent("chinese",llm_config={"config_list":config_list_mistral},system_message="你是一个知识渊博的中国人，你要向大家介绍中国文化",max_consecutive_auto_reply=1)
american=autogen.AssistantAgent("",llm_config={"config_list":config_list_mistral},system_message="你是一个知识渊博的美国人，你要向大家介绍美国文化",max_consecutive_auto_reply=1)
korea=autogen.AssistantAgent("chinese",llm_config={"config_list":config_list_mistral},system_message="你是一个知识渊博的韩国人，你要向大家介绍韩国文化",max_consecutive_auto_reply=1)

host=autogen.UserProxyAgent("host",llm_config={"config_list":config_list_mistral},code_execution_config={"work_dir": "coding","use_docker": False})
#您可以要求此代理使用 generate_reply 方法生成对问题的响应
reply = host.generate_reply(messages=[{"content": "请你们各自介绍一下你们国家的文化", "role": "user"}])
print(reply)


