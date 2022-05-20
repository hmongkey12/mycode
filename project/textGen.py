import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
# initialize tokenizer and model from pretrained GPT2 model
sequence = "It was a clear black night. The streets where filled with rats.  The criminals came out to do crime.  The man in the mask was there to stop them."
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
inputs = tokenizer.encode(sequence, return_tensors='pt')
outputs = model.generate(
    inputs, max_length=200, do_sample=True, top_k=50
)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)
