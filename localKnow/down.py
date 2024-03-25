#模型下载
from modelscope import snapshot_download
# model_dir = snapshot_download('ZhipuAI/chatglm3-6b',cache_dir="D:\modelscope")
# model_dir

#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('Jerry0/text2vec-base-chinese')

print(model_dir)
# model_dir = snapshot_download("ZhipuAI/chatglm3-6b", revision = "v1.0.0")
# tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
# model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)
# response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
# print(response)