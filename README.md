## Large Language Model Exploration
- Inference (Failed to make as much progress with it, Retrieval-Augmented Generation(RAG) still a work in progress)
- Embedding (Mainly Focused here, using cosine similarity to do semantic segmentation and categorical classification)
- Zero-Shot Classification (Application, as in being used, but the training is not explored yet for now!)
- Training of Models (Halfway there but lacking of GPU power to do extensively and test more, could use [Google Colab](https://colab.google/) or something else!, to be found!)

### Inference
- Mainly Explored using Azure OpenAI, OpenAI and meta-llama (Not much explored due to local-LLM limitation being local computing power)
- RAG and training is to be done!

### Embedding
- Explored many open source LLM models and had to do some naive method of mean pooling or cls pooling for sentence embedding from word embedding
- Used for semantic segmentation, using cosine similarity, referenced heavily from [Naveed Afzal here](https://www.naveedafzal.com/posts/an-introduction-to-unsupervised-topic-segmentation-with-implementation/)
- Used cosine similarity as well for categorical classification by matching similarity to slot into categories
- Query vs Document embedding is something i would want to look into as well for information retrieval task!

### Zero-Shot Classification
- Explored using this method of classification as there were lacking data points to work on to train from for now
- Would like to explore more of this classification in the future and the training using available data and computing power, to explore training based off the "Contradiction", "Neutral" and "Entailment" labelling
- Feels like the concept is just ~~Binary~~ Trinary Classification and yea!!

### Training
- TO BE DONE!


# README WILL BE IMPROVED UPON LATER ON!