import torch
import math
import numpy as np
def get_length(embedding_1d):
    sum = 0
    for i in embedding_1d:
        sum+=(i**2)
    return math.sqrt(sum)
def normalise_embedding(embedding_1d):
    length = get_length(embedding_1d)
    for i in range(len(embedding_1d)):
        embedding_1d[i] /= length
def get_normalise_embedding(embedding_1d):
    if type(embedding_1d) is torch.Tensor:
        temp_embedding_1d = (embedding_1d.detach().numpy()).copy()
    else:
        temp_embedding_1d = embedding_1d.copy()
    length = get_length(temp_embedding_1d)
    for i in range(len(temp_embedding_1d)):
        temp_embedding_1d[i] /= length
    return temp_embedding_1d




def cosine_sim(embedding_1, embedding_2):
    embedding_1 = get_normalise_embedding(embedding_1)
    embedding_2 = get_normalise_embedding(embedding_2)
    sim_sum = 0
    for e_1, e_2 in zip(embedding_1, embedding_2):
        sim_sum += (e_1*e_2)
    return sim_sum
def norm_ed_cosine_sim(embedding_1, embedding_2):
    sim_sum = 0
    for e_1, e_2 in zip(embedding_1, embedding_2):
        sim_sum += (e_1*e_2)
    return sim_sum
def generic_sent_cos_sim(model_emb_func, t1, t2, additional_nesting = False):
    if additional_nesting:
        return cosine_sim(model_emb_func(t1)[0], model_emb_func(t2)[0])    
    return cosine_sim(model_emb_func(t1), model_emb_func(t2))

def test_emb_model(model_emb_func, sent_pair_comparison_list, sorting = False, additional_nesting = False):
    ending_dict = {}
    for comp1, comp2 in sent_pair_comparison_list:
        ending_dict[(comp1, comp2)] = generic_sent_cos_sim(model_emb_func, comp1, comp2, additional_nesting)
    if sorting:
        sorted_ending_dict = {comps:comps_res for comps, comps_res in (sorted(ending_dict.items(), key=lambda dict_item: dict_item[1], reverse = True))}
        return sorted_ending_dict
    return ending_dict
def test_emb_model_results(ending_dict, sorting = False):
    print("Similarity level:")
    #res_sum = 0
    if sorting:
        for comps, res in (sorted(ending_dict.items(), key= lambda dict_item: dict_item[1], reverse=True)):
            ## print(f"{comps[0]:20.5}-{comps[1]:5.20}: {res:.5}") # "{:min_pad.max_pad}", max pad is essentially also the max number of chars permitted!!
            print(f"{comps[0]:20.20} /-/ {comps[1]:20.20} : {res:.5}")
            #res_sum += res
    else:
        for comps, res in ending_dict.items():
            ## print(f"{comps[0]:20.5}-{comps[1]:5.20}: {res:.5}") # "{:min_pad.max_pad}", max pad is essentially also the max number of chars permitted!!
            print(f"{comps[0]:20.20} /-/ {comps[1]:20.20} : {res:.5}")
            #res_sum += res
        
    ## res_sum no purpose and stuff yet since no measure of accuracy present, like it should/should not match, dont know so cannot say the sum is good or not, etc or avg, but later on can try with these and maybe weighted based on certain comparisons more impt?
     
     
        
# eg:
## function is "get_sentenceS_embedding"
## comparison list is "comparison_pair_list"
res_dict = test_emb_model(get_sentenceS_embedding, comparison_pair_list, sorting=False , additional_nesting=True)
test_emb_model_results(res_dict, sorting=True)
comparison_pair_list = [("tax relief", "employee benefit"), ("tax relief for employees", "employee benefit"), ("the world is green", "i hate soda")]
comparison_pair_list.append(("yearly flight tickets home for employees", "home passage"))
comparison_pair_list.append(("yearly flight tickets home for employees", "subsidised flights to employee home country"))
comparison_pair_list.append(("night shift", "overtime pay"))
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
# normalise tensor, but i think 1d tensor cannot? need to be inside another tensor to work?? idk, need read on docs or more maybe!
sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)







## generic useful for example: model is "BAAI/bge-large-en-v1.5"
# model loading and eval?? are stuff to look at and maybe train further if can... but this one need look... idk how also... need read docs etc and look...
# pooling and normalisation!!


from transformers import AutoTokenizer, AutoModel
import torch

# Load model from HuggingFace Hub
#tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-large-zh-v1.5')
#model = AutoModel.from_pretrained('BAAI/bge-large-zh-v1.5')
tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-large-en-v1.5")
model = AutoModel.from_pretrained("BAAI/bge-large-en-v1.5")

model.eval()

# Sentences we want sentence embeddings for
#sentences = ["样例数据-1", "样例数据-2"]
sentences = ["i like you", "i want to kill you"]

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
# for s2p(short query to long passage) retrieval task, add an instruction to query (not add instruction for passages)
# encoded_input = tokenizer([instruction + q for q in queries], padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)
    # Perform pooling. In this case, cls pooling.
    sentence_embeddings = model_output[0][:, 0]
# normalize embeddings
sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
print("Sentence embeddings:", sentence_embeddings)
