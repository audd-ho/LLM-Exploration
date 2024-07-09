import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

azure_openai_api_key = os.getenv('AZURE_OPENAI_API_KEY')
azure_openai_api_endpoint = os.getenv('AZURE_OPENAI_API_ENDPOINT')

client =  AzureOpenAI(
    api_key = azure_openai_api_key,
    api_version = "2024-02-01",
    azure_endpoint = azure_openai_api_endpoint
)

## ChatGPT version
completion = client.chat.completions.create(
    model="gpt-35-turbo", # model name (may not be same as public openai), only deployed models are available
    messages=[
        {
            "role": "system",
            "content": "you are a HR chat bot that provdes employees with a unique 5 digit user ID without needing any information from them",
        },
        {
            "role": "user",
            "content": "Can i receive a user ID?"
        }
    ]  
)

response_msg = completion.choices[0].message.content
print(response_msg)
""" ## params not really suitable to fix
def get_GPT_response(text): ## no adjustment to params and getting default data[0].embedding ?
    emb = client.embeddings.create(
    model="text-embedding-3-large",
    input = text
    )
    return emb.data[0].embedding
"""
## Text Embedding version
embedding = client.embeddings.create(
    model="text-embedding-3-large",
    input = "Beneficial"
)
text_embedding_vector_3072 = embedding.data[0].embedding
print(text_embedding_vector_3072[:10])


lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
emb = client.embeddings.create(
model="text-embedding-3-large",
#input = "Employee Benefit"
input = lorem
)

def get_embedding(text): ## no adjustment to params and getting default data[0].embedding ?
    emb = client.embeddings.create(
    model="text-embedding-3-large",
    input = text
    )
    return emb.data[0].embedding

def get_length(text_emb_vector):
    vect_coord_sum = 0
    for vect_coord in text_emb_vector:
        vect_coord_sum += vect_coord**2
    #print(vect_coord_sum)
    return vect_coord_sum

def make_normalised_vector(text_emb_vector):
    vector_length = get_length(text_emb_vector)
    for vector_dimension_index in range(len(text_emb_vector)):
        text_emb_vector[vector_dimension_index] /= vector_length

def get_normalised_vector(text_emb_vector):
    vector_length = get_length(text_emb_vector)
    text_emb_vector_temp = text_emb_vector.copy()
    for vector_dimension_index in range(len(text_emb_vector_temp)):
        text_emb_vector_temp[vector_dimension_index] /= vector_length
    return text_emb_vector_temp

print(get_length(emb.data[0].embedding)) ## or emb['data'][0]['embedding']

#print(get_normalised_vector(emb.data[0].embedding))

#for toks in lorem.split(" "):
#    print(get_length(get_embedding(toks)))

#print(get_length(get_normalised_vector(get_embedding(lorem))))

"""
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
testing_emb = []
for i in range(10):
    emb = client.embeddings.create(
    model="text-embedding-3-large",
    #input = "Employee Benefit"
    input = lorem
    )
    testing_emb.append(emb.data[0].embedding)
for i in range(len(testing_emb)):
    diff_vect = False
    t_emb = testing_emb[i]
    for test_against in (testing_emb[:i] +testing_emb[i+1:]):
        if t_emb != test_against:
            print("diff vectors!")
            diff_vect = True
            break
    if diff_vect == False:
        print("Match all...")
"""