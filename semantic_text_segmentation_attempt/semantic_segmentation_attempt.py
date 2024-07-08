from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

#sentences = ["This is an example sentence", "Each sentence is converted"]
#embeddings = model.encode(sentences)
def get_sentence_embedding(sentence):
    return model.encode(sentence)


''


sents = "random inout abc"
sents = sents.split(" ")


''


from itertools import islice

def window(seq, n=3):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
        

''


WINDOW_SIZE = 3
window_size_split = list(window(sents, WINDOW_SIZE))
print(window_size_split)
window_splited_texts = [' '.join([window_toks for window_toks in each_window]) for each_window in window_size_split]
print(window_splited_texts)
window_splited_text_embs = get_sentence_embedding(window_splited_texts)


''


coherence_scores = [norm_ed_cosine_sim(pair[0], pair[1]) for pair in zip(window_splited_text_embs, window_splited_text_embs[1:])]


''


import matplotlib.pyplot as plt
plt.plot(coherence_scores)


'''
## index of split => index1, index2, index3, if lowest means 1 and 3 diff topic? so split up and 2 can just follow either or be left out?
intervals_indexes = [0] + [ind+(WINDOW_SIZE-1) for ind in split_indexes] + [len(sents)]
intervals_indexes

segment_indexes = list(zip(intervals_indexes[:-1], intervals_indexes[1:]))
segment_indexes

sent_segments = [" ".join(sents[seg_ind[0]:seg_ind[1]]) for seg_ind in segment_indexes]
sent_segments
'''


def climb_v1(co_score_list, list_index, mode = "l"):
    res_score = 0
    if mode == "l":
        while (list_index >= 0):
            if co_score_list[list_index] > res_score:
                res_score = co_score_list[list_index]
                list_index -= 1
            else:
                break
        return res_score
    else:
        list_len = len(co_score_list)
        while (list_index < list_len):
            if co_score_list[list_index] > res_score:
                res_score = co_score_list[list_index]
                list_index += 1
            else:
                break
        return res_score
    
    
def depth_score_v1(co_score_list):
    res_depth_score_list = []
    co_score_len = len(co_score_list)
    for i in range(co_score_len):
        i_co_score = co_score_list[i]
        l_peak = climb_v1(co_score_list, i, "l")
        r_peak = climb_v1(co_score_list, i, "r")
        i_depth_score = 0.5 * (l_peak + r_peak - (2*i_co_score))
        res_depth_score_list.append(i_depth_score)
    return res_depth_score_list

depth_score_v1_list = depth_score_v1(coherence_scores)

plt.plot(depth_score_v1_list)

from scipy.signal import argrelmax

def get_local_maxima(depth_scores, order=1):
    maxima_ids = argrelmax(depth_scores, order=order)[0]
    filtered_scores = np.zeros(len(depth_scores))
    filtered_scores[maxima_ids] = depth_scores[maxima_ids]
    return filtered_scores
 
 
filtered_scores_list = get_local_maxima(np.array(depth_score_v1_list), order=1)
filtered_scores_list

plt.plot(filtered_scores_list)

def compute_threshold(scores):
    s = scores[np.nonzero(scores)]
    threshold = np.mean(s) - (np.std(s) / 2)
    # threshold = np.mean(s) - (np.std(s))
    return threshold
 
filtered_list_threshold = compute_threshold(filtered_scores_list)

fsl_len = len(filtered_scores_list)
plt.plot(filtered_scores_list)
plt.plot([filtered_list_threshold for i in range(fsl_len)])
plt.show()

def get_threshold_segments(scores, threshold=0.1):
    segment_ids = np.where(scores >= threshold)[0]
    return segment_ids
segment_ids = get_threshold_segments(filtered_scores_list, filtered_list_threshold)
segment_ids


''''''

new_segment_ids = [0] + [(ids+(WINDOW_SIZE-1)) for ids in segment_ids] + [len(sents)]
new_segment_ids_intervals = list(zip(new_segment_ids[:-1], new_segment_ids[1:]))
new_sent_id_segments = [" ".join(sents[seg_ind[0]:seg_ind[1]]) for seg_ind in new_segment_ids_intervals]
new_sent_id_segments


''''''

def test_to_see(new_sent_id_segments_input, category_text):
    comparison_list = [(c1, c2) for c1,c2 in zip(new_sent_id_segments_input, [category_text for i in range(len(new_sent_id_segments_input))])]
    res_dict = test_emb_model(get_sentence_embedding, comparison_list, sorting=False , additional_nesting=False)
    test_emb_model_results(res_dict, sorting=True)