from transformers import pipeline, set_seed

generator = pipeline('text-generation', 
model='gpt2')

set_seed(42)

result = generator("New York is a city, ", max_length=30, num_return_sequences=5)

print(result)