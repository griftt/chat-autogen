import os.path
from langchain.chains.retrieval_qa.base import RetrievalQA

#文件加载
from langchain_community.document_loaders import  DirectoryLoader
#文件拆分
from  langchain.text_splitter import  CharacterTextSplitter
#embbing
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma
#提取文档做qa

from langchain.llms.ollama import Ollama





def load_document(dic="book"):
    loader=DirectoryLoader(dic,show_progress=True)
    documents=loader.load()
    print(len(documents))
    #拆分
    #chunk_overlap，步进距离  例如 abc bcd
    text_spliter= CharacterTextSplitter(chunk_size=256,chunk_overlap=0)
    docs=text_spliter.split_documents(documents)
    print(docs)
    return docs

def load_embedding_mode(model_name="text2vec3"):
    encode_kwargs={"normalize_embeddings":False}
    model_kwargs={"device":"cuda:0"}
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

def store_chroma(docs, embedding, persist_dir="VectorStore"):
    db=Chroma.from_documents(docs,embedding,persist_directory=persist_dir)
    db.persist()
    return  db



#documents=load_document()

embedding_model=load_embedding_mode("C:\\Users\\13612\\.cache\\modelscope\\hub\\Jerry0\\text2vec-base-chinese")

if not os.path.exists("VectorStore"):
    docs=load_document()
    db=store_chroma(docs,embedding_model)
else:
    #db =Chroma(collection_name="VectorStore")
    docs = load_document()
    db = store_chroma(docs, embedding_model)


retrieval_qa=db.as_retriever()
llm=Ollama(
    base_url="http://localhost:11434",
    model="mistral",
)


qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retrieval_qa
)

data= qa.invoke("mysql 数据库的索引原理是什么")
print(data)

