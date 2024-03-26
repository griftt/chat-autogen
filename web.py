from typing import Optional

import streamlit as st
import numpy as np
import pandas as pd
import time
import autogen
import streamlit as st
from typing import Optional, Any, List, Dict, Union, Tuple
from autogen import ChatResult, Agent, ConversableAgent

from config_list import config_list_mistral


# st.sidebar.page_link("web.py", label="Home", icon="🏠")
# st.sidebar.page_link("pages/llm.py", label="Page 1", icon="1️⃣")
# st.sidebar.page_link("pages/know.py", label="Page 2", icon="2️⃣")
# st.sidebar.page_link("http://www.google.com", label="Google", icon="🌎")
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
                                      human_input_mode="ALWAYS",
                                      # llm_config={"config_list": config_list_mistral},
                                      code_execution_config={"work_dir": "coding",
                                                             "use_docker": False})
        host.register_reply([Agent, None], reply_func=callBack)
        host.initiate_chat(chinese, message=promt, max_turns=2)

#左侧的提交表格
st.title('Griftt 的 :blue[智能管家] :sunglasses:',anchor ='false')
st.sidebar.title(' :blue[基础设置] :',anchor ='false')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

form = st.sidebar.form("my_form")
form.slider("Inside the form")
form.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Now add a submit button to the form:
form.form_submit_button("Submit")



#main
tab1, tab2 = st.tabs(["📈 人机互动", "🗃 AI群聊"])
tab1.subheader("在这里调试你的一对一人机互动操作")
#选择需要使用的大模型
#单聊

model=tab1.selectbox(
    "选择你的Ai模型",
    ("Email", "Home phone", "Mobile phone")
)
konwledge=tab1.selectbox(
    "选择你的知识库",
    ("Email", "Home phone", "Mobile phone")
)

msgContainer = tab1.container(height=400)
#初始化消息框
if "messages" not in  st.session_state:
    st.session_state.messages=[]

#打印出原有的历史消息
for message in st.session_state.messages:
    # with tab1.chat_message(message["role"]):
    msgContainer.chat_message(message["role"]).markdown(message["content"])
st.write(st.session_state.messages)
#初始化聊天
simpleChat=SimpleChat()
def callBack(recipient: ConversableAgent,
                    messages: Optional[List[Dict]] = None,
                    sender: Optional[Agent] = None,
                    config: Optional[Any] = None,
                ) :

    if messages is not None and messages[-1] is not None:
        print("Dddd", messages)
        msgContainer.chat_message("AI").write(messages[-1]["content"])
        #     st.session_state.messages.append({"role": "AI", "content": message["content"]})
        st.session_state.messages.append({"role": messages[-1]["role"], "content": messages[-1]["content"]})

    return (True, None)




if prompt := tab1.chat_input("输入你的问题"):

    msgContainer.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 调用接口去查询api
    simpleChat.initSimeDoubleChat(prompt)
    # for message in result.chat_history:
    #
    #     msgContainer.chat_message("AI").write(message["content"])
    #     st.session_state.messages.append({"role": "AI", "content": message["content"]})


    # messages.chat_message("AI").write(f"{prompt}")

    # with tab1.chat_message("user"):
    #     msgContainer.markdown(prompt)
    # Add user message to chat history




tab2.subheader("AI团队帮你完成任务")



# Delete all the items in Session state
# for key in st.session_state.keys():
#     del st.session_state[key]