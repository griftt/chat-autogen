from typing import Optional, Any, List, Dict, Union, Tuple

import autogen
from autogen import ChatResult, Agent, ConversableAgent

from autogenDmo.simpleChat import callBack
from config_list import config_list_mistral



def callBack(
                    recipient: ConversableAgent,
                    messages: Optional[List[Dict]] = None,
                    sender: Optional[Agent] = None,
                    config: Optional[Any] = None,
                ) :
    if messages is not None and messages[-1] is not None:
        print("Dddd", messages[-1]["content"])
        st.session_state.messages.append({"role": "AI", "content": messages[-1]["content"]})

    return (True, None)

class SimpleChat:
    def initSimeDoubleChat(self,promt) :
        chinese = autogen.AssistantAgent("chinese", llm_config={"config_list": config_list_mistral},
                                         system_message="you good at math",
                                         max_consecutive_auto_reply=1)
        # american = autogenUtil.AssistantAgent("", llm_config={"config_list": config_list_mistral},
        #                                   system_message="你是一个知识渊博的美国人，你要向大家介绍美国文化",
        #                                   max_consecutive_auto_reply=1)
        # korea = autogenUtil.AssistantAgent("chinese", llm_config={"config_list": config_list_mistral},
        #                                system_message="你是一个知识渊博的韩国人，你要向大家介绍韩国文化",
        #                                max_consecutive_auto_reply=1)

        host = autogen.UserProxyAgent("host",
                                      # llm_config={"config_list": config_list_mistral},
                                      code_execution_config={"work_dir": "coding",
                                                             "use_docker": False})
        host.register_reply([Agent, None], reply_func=callBack)
        host.initiate_chat(chinese, message=promt, max_turns=2)




