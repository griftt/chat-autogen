import autogen
from autogen import AssistantAgent, UserProxyAgent
from autogen import GroupChat
from autogen import GroupChatManager
from autogen import Agent, ConversableAgent
from config_list import config_list_gpt3
from DrissionPage import ChromiumPage
import tempfile
from typing import Optional, Any, List, Dict, Union, Tuple
#config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
import json
from DrissionPage._pages.chromium_page import ChromiumPage  # 导入 ChromiumPage 类，确保路径和导入正确

# class ChromiumPageModel(BaseModel):
#     name: str
#     chromium_page: ChromiumPage
#
#     def __init__(self, name: str, chromium_page: ChromiumPage):
#         self.name=name
#         self.chromium_page=chromium_page
#
#     # class Config:
#     #     arbitrary_types_allowed = True  # 允许任意类型的字段
#
#     #@classmethod
#     # def __get_pydantic_core_schema__(cls, model, schema_registry):
#     #     # 实现对 ChromiumPage 类的模型生成逻辑
#     #     return {
#     #         'title': 'ChromiumPageModel',
#     #         'type': 'object',
#     #         'properties': {
#     #             'chromium_page': schema(model.chromium_page)
#     #         },
#     #         'required': ['chromium_page'],
#     #     }

# 创建 ChromiumPageModel 实例
print(json.dumps(ChromiumPage().dict(), indent=4))
