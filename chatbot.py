
from transformers import pipeline

chatbot = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

print("AI Chatbot Started (type 'exit' to stop)")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    prompt = "Answer the question: " + user

    response = chatbot(prompt, max_length=100)

    print("Bot:", response[0]['generated_text'])


























    
    # from transformers import pipeline

# # Load chatbot model
# chatbot = pipeline("text-generation", model="gpt2")

# print("Chatbot started (type exit to stop)\n")

# while True:
    
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     response = chatbot(user_input, max_length=50)

#     print("Bot:", response[0]['generated_text'])
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# model_name = "microsoft/DialoGPT-small"

# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# print("Chatbot started (type 'exit' to stop)")

# chat_history_ids = None

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

#     bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

#     chat_history_ids = model.generate(
#         bot_input_ids,
#         max_length=1000,
#         pad_token_id=tokenizer.eos_token_id
#     )

#     response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

#     print("Bot:", response)
# from transformers import pipeline

# chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

# print("Chatbot started (type 'exit' to stop)")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     response = chatbot(user_input, max_length=100)

#     print("Bot:", response[0]['generated_text'])
# from transformers import pipeline

# chatbot = pipeline("text-generation", model="google/flan-t5-base")

# print("Chatbot started (type 'exit' to stop)")

# while True:
#     user = input("You: ")

#     if user.lower() == "exit":
#         break
#     prompt = f"Answer the following question:{user}"

#     result = chatbot(user, max_new_tokens=100)

#     print("Bot:", result[0]["generated_text"].replace(prompt,"").strip())
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# import torch

# model_name = "google/flan-t5-large"

# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# print("Chatbot started (type 'exit' to stop)")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     prompt = "Answer the question: " + user_input

#     inputs = tokenizer(prompt, return_tensors="pt")

#     outputs = model.generate(**inputs, max_new_tokens=100)

#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     print("Bot:", response)
# from transformers import pipeline

# chatbot = pipeline(
#     "text-generation",
#     model="google/flan-t5-small"
# )

# print("Chatbot started (type 'exit' to stop)")

# while True:
#     user = input("You: ")

#     if user.lower() == "exit":
#         break

#     prompt = f"Question: {user} Answer:"

#     result = chatbot(prompt, max_new_tokens=100)

#     answer = result[0]["generated_text"].replace(prompt, "")

#     print("Bot:", answer.strip())
# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

# model_name = "microsoft/DialoGPT-medium"

# # Load tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# print("Chatbot started (type 'exit' to stop)")

# chat_history_ids = None

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     # Encode user input
#     new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

#     # Append to chat history
#     bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids

#     # Generate response
#     chat_history_ids = model.generate(
#         bot_input_ids,
#         max_length=1000,
#         pad_token_id=tokenizer.eos_token_id,
#         do_sample=True,
#         top_k=50,
#         top_p=0.95
#     )

#     # Decode bot response
#     bot_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

#     print("Bot:", bot_response)

########################################################################################
