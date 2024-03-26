import tempfile
from typing import Optional, Any, List, Dict, Union, Tuple

import autogen
from autogen import ChatResult, Agent, ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

from autogenDmo.simpleChat import callBack
from config_list import config_list_mistral
import streamlit as st
from typing import Annotated, Literal


##计算工具
Operator = Literal["+", "-", "*", "/"]
def calculator(a: int, b: int, operator: Annotated[Operator, "operator"]) -> int:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return int(a / b)
    else:
        raise ValueError("Invalid operator")
# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
)
def callBack(
                    recipient: ConversableAgent,
                    messages: Optional[List[Dict]] = None,
                    sender: Optional[Agent] = None,
                    config: Optional[Any] = None,
                ) :
    # if messages is not None and messages[-1] is not None:
    #     print("111", messages[-1]["content"])
    #     st.session_state.messages.append({"role": "AI", "content": messages[-1]["content"]})
    #     st.session_state.msgContainer.chat_message("AI").write(messages[-1]["content"])

    return (True, None)

class SimpleChat:
    def initSimeDoubleChat(self,promt):
        chinese = autogen.AssistantAgent("chinese", llm_config={"config_list": config_list_mistral},
                                         system_message="你是一个顶级程序员"
                                         )
        # Register the tool signature with the assistant agent.
        #注册让助手可以建议用户代理调用
        chinese.register_for_llm(name="calculator", description="A simple calculator")(calculator)


        # american = autogenUtil.AssistantAgent("", llm_config={"config_list": config_list_mistral},
        #                                   system_message="你是一个知识渊博的美国人，你要向大家介绍美国文化",
        #                                   max_consecutive_auto_reply=1)
        # korea = autogenUtil.AssistantAgent("chinese", llm_config={"config_list": config_list_mistral},
        #                                system_message="你是一个知识渊博的韩国人，你要向大家介绍韩国文化",
        #                                max_consecutive_auto_reply=1)
        #简单调用工具
        host = autogen.UserProxyAgent("host",
                                      max_consecutive_auto_reply=4,
                                      # llm_config={"config_list": config_list_mistral},
                                      human_input_mode="NEVER",
                                      code_execution_config={"executor": executor,})
        host.register_reply([Agent, None], reply_func=callBack)
        # Register the tool function with the user proxy agent.
        #用户代理可以调用的方法
        host.register_for_execution(name="calculator")(calculator)

        from autogen import register_function

        # Register the calculator function to the two agents.
        #也可以通过这个方法向两个代理注册工具
        # register_function(
        #     calculator,
        #     caller=assistant,  # The assistant agent can suggest calls to the calculator.
        #     executor=user_proxy,  # The user proxy agent can execute the calculator calls.
        #     name="calculator",  # By default, the function name is used as the tool name.
        #     description="A simple calculator",  # A description of the tool.
        # )

        host.initiate_chat(chinese,message="帮我写程序计算从1 加到100 总和是多少", max_turns=4)

        #host.send(promt,chinese)


caht=SimpleChat()
caht.initSimeDoubleChat("1+11等于多少")
