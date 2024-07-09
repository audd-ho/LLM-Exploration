# Import Azure OpenAI
import os
from dotenv import load_dotenv

## chat completion, turbo
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

## text embedding
from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()

## langchain for chat completion, turbo

#print(os.environ["AZURE_OPENAI_API_KEY"])
#print(os.environ["AZURE_OPENAI_ENDPOINT"])

#print(os.environ["OPENAI_API_VERSION"])
#print(os.environ["AZURE_OPENAI_API_VERSION"])

# Create an instance of Azure OpenAI
# Replace the deployment name with your own
llm = AzureChatOpenAI(
    #deployment_name="gpt-35-turbo",
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"]
    # model
    # deployment
    # openai_api_version
    # openai_api_key
    # azure_endpoint
)

c_template = ChatPromptTemplate.from_messages([
    ("system", "You are a HR to provide users with a unique employee ID, based on their name"),
    ("user", "My name is {some_name}, please provide me an ID"),
    ("assistant", "Hold on a second while I attempt to provide you with a unique ID like {some_id}, but different from {some_id}"),
    ("user", "Okay, please hurry up, i'm waiting"),
    ("ai", "Please don't rush me"),
    ("human", "Okay, i'm waiting still")
])

c_prompt = c_template.invoke(
    {
        "some_name": "poppy",
        "some_id": "123"
    }
)

temp_resp = llm.invoke(c_prompt)
print(temp_resp.content)

"""
# Run the LLM
response = llm.invoke(["When did PM Lee of singapore pass on his position?"])

print(llm)

print(response)



response = llm.invoke(["When did PM Lee of singapore pass on his position?", "When did PM Pee of singapore pass on his position?", "When did PM Low of singapore pass on his position?", "How did abraham lincoln pass?", "What colour is the sea?"])

print(response)

response = llm.invoke("When did PM Lee of singapore pass on his position?")

print(response)
"""

## langchain for text embedding

llm_embedding = AzureOpenAIEmbeddings(
    #deployment_name="gpt-35-turbo",
    azure_deployment=os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"]
)

"""
text = "this is a test document for embedding"
query_result = llm_embedding.embed_query(text)
print(query_result[:5])

doc_result = llm_embedding.embed_documents([text])
print(doc_result[1:])

print(doc_result[0][:5])

print(query_result == doc_result[0])
"""
