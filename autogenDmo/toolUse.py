import autogen
from autogen import AssistantAgent, UserProxyAgent
from autogen import GroupChat
from autogen import GroupChatManager
from autogen import Agent, ConversableAgent
from config_list import config_list_gpt3
from DrissionPage import ChromiumPage
import tempfile
from typing import Optional, Any, List, Dict, Union, Tuple,Type,Annotated
#config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
from pydantic import BaseModel,GetCoreSchemaHandler,schema
from DrissionPage._pages.chromium_page import ChromiumPage  # 导入 ChromiumPage 类，确保路径和导入正确



# class ChromiumPageModel(BaseModel):
#     name: str
#     chromium_page : ChromiumPage
#
#     def __init__(self,name, chromium_page=None):
#         self.name = name
#         if chromium_page is None:
#             self.chromium_page = ChromiumPage()
#         else:
#             self.chromium_page = chromium_page
#
#     @classmethod
#     def __get_pydantic_core_schema__(cls, model, schema_registry):
#         # 实现对 ChromiumPage 类的模型生成逻辑
#         return {
#             'title': 'ChromiumPageModel',
#             'type': 'object',
#             'properties': {
#                 'chromium_page': schema(model.chromium_page)
#             },
#             'required': ['chromium_page'],
#         }




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


#
# 打开一个指定页面
# 
#
#
def openPage(url:str)->str:
    page = ChromiumPage()
    # 跳转到登录页面
    return  page.get(url)



def login_gitee(url:str,account:str,password:str )->str:
    page= ChromiumPage()
    # 跳转到登录页面
    page.get(url)
    # 定位到账号文本框，获取文本框元素
    ele = page.ele('#user_login')
    # 输入对文本框输入账号
    ele.input(account)
    # 定位到密码文本框并输入密码
    page.ele('#user_password').input(password)
    # 点击登录按钮
    page.ele('@value=登 录').click()
    return  page.html()


def Open_a_web_browser()->str:
    # 创建页面对象，并启动或接管浏览器
    ChromiumPage()
    return "OK"




user_proxy = UserProxyAgent("user_proxy", llm_config={"config_list": config_list_gpt3},human_input_mode="NEVER",
                            code_execution_config={"work_dir": "coding","use_docker": False})

brower_worker = AssistantAgent("brower_worker", system_message="你是一个顶级的python工程师,你可以灵活调用我注册的已有方法来完成所有对浏览器的操作,当我需要你进行浏览器操作时，请记住你要先调用方法打开一个浏览器，所有操作都要基于浏览器进行操作" , llm_config={"config_list": config_list_gpt3},human_input_mode="NEVER",
                            code_execution_config={"work_dir": "coding","use_docker": False})

brower_worker.register_for_llm(name="Open_a_web_browser", description="Open a web browser and Return ther Model ChromiumPageModel ")(Open_a_web_browser)
brower_worker.register_for_llm(name="login_gitee", description=" log in to Gitee ")(login_gitee)

user_proxy.register_for_execution(name="Open_a_web_browser")(Open_a_web_browser)
user_proxy.register_for_execution(name="login_gitee")(login_gitee)
user_proxy.initiate_chat(brower_worker, message=" 13538774847 is my gitee account,1415wsh52000 is my gitee pawwarod ,please use them to  log in to Gitee ", max_turns=4)


# group_chat = GroupChat(
#     agents=[assistant, coder,test],
#     messages=[],
#     max_round=6,
# )
#
# group_chat_manager = GroupChatManager(
#     groupchat=group_chat,
#     system_message="give them a interger number",
#     llm_config={"config_list":config_list_gpt3},
# )
# #user_proxy.initiate_chat(assistant, message="")
# #现在我们创建一个 GroupChatManager 对象，并提供 GroupChat 对象作为输入。我们还需要指定群组聊天管理器的 llm_config ，以便它可以使用LLM来选择下一个代理（ auto 策略）。
# chat_result = user_proxy.initiate_chat(
#     group_chat_manager,
#     message="每个人告诉我一个数字",
#     summary_method="reflection_with_llm",)

# if __name__ == '__main__':
#     chromium_page_schema = ChromiumPage().__get_pydantic_core_schema__()
#     print(chromium_page_schema)