"""
## for masking!!

# Load model directly
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
model = AutoModelForMaskedLM.from_pretrained("google-bert/bert-base-uncased")
"""

## model for embedding!!

from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained("bert-base-uncased")


"""
text = ["abc"]

# Tokenize and encode text using batch_encode_plus
# The function returns a dictionary containing the token IDs and attention masks
encoding = tokenizer.batch_encode_plus(
    text,                    # List of input texts
    padding=True,              # Pad to the maximum sequence length
    truncation=True,           # Truncate to the maximum sequence length if necessary
    return_tensors='pt',      # Return PyTorch tensors
    add_special_tokens=True    # Add special tokens CLS and SEP
)

print(encoding) 

input_ids = encoding['input_ids']  # Token IDs
# print input IDs
print(f"Input ID: {input_ids}")
attention_mask = encoding['attention_mask']  # Attention mask
# print attention mask
print(f"Attention mask: {attention_mask}")


# Generate embeddings using BERT model
with torch.no_grad(): ## need import torch if want use/do this
    outputs = model(input_ids, attention_mask=attention_mask)
    word_embeddings = outputs.last_hidden_state  # This contains the embeddings

# Decode the token IDs back to text
decoded_text = tokenizer.decode(input_ids[0], skip_special_tokens=True)
#print decoded text
print(f"Decoded Text: {decoded_text}")

"""

text = "abc123"

# Tokenize the text again for reference
tokenized_text = tokenizer.tokenize(text)
#print tokenized text
print(f"tokenized Text: {tokenized_text}")
# Encode the text
encoded_text = tokenizer.encode(text, return_tensors='pt')  # Returns a tensor
# Print encoded text
print(f"Encoded Text: {encoded_text}")

encoded_text_plus = tokenizer.encode_plus(text, return_tensors='pt')
print(encoded_text_plus)

output = model(encoded_text)
print("#1: ", output)

##output = model(**encoded_text) ## cannot cos "argument after ** must be a mapping, not Tensor"
##print("#2: ", output)

##output = model(encoded_text_plus)
##print("#3: ", output)

output = model(**encoded_text_plus)
print("#4: ", output)