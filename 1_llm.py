# pip install ollama 

import ollama
import json
llm_model = 'llama3.2:latest'
text = "Generative AI refers to a category of artificial intelligence systems designed to create new content, such as text, images, music, or even videos that mimics or is inspired by existing data. These systems learn patterns, styles, and structures from large datasets and use that knowledge to generate original outputs. Unlike traditional AI, which might focus on analyzing or classifying data, generative AI is about producing something new."
prompt = f"What is generative AI? Explain in 100 words: {text}"
response = ollama.generate(llm_model, prompt)
print(response['response'])


# model + prompt/query(Context) + input => response

# Audio File => Transcription => prompt + data ==> model ==> response

# prompt + data ==> model ==> response


# def run_ollama_prompt(prompt, llm_model):
#     response = ollama.generate(llm_model, prompt)
#     response_text = response['response']
#     return response_text
#     #return response 

# # result = run_ollama_prompt("What is PIP",llm_model)
# # print(result)

# # #-------------------------------------------------
# # # query = input('Enter your question:')
# # # def sample_call(llm_model,query):
# # #     print("=" * 100)
# # #     print("Running sample call with query:", query)
# # #     prompt = f"Answer the following question: {query}"
# # #     response = run_ollama_prompt(prompt, llm_model)
# # #     print("Response:", response)
# # #     return response
# # # sample_call(llm_model,query)

# # LLM Model request cost= Context + Prompt + Response
# # #-------------------------------------------------

# # paragraph => keywords, topics
# def extract_keywords(transcription, llm_model):
#     print("=" * 100)
#     print("Extracting keywords and topics...")

#     extract_kwrds_prompt = f"""
#     From the following text, extract and return the following two categories of information:
#         1. keywords: Keywords, Named Entities,places, name of cities, names of people, dates, events, products, objects, tools or physical items or important keyword.
#         2. topics: extract the main topics in transcription. Ensure that the topics are broad.

#         Do not give any explanations or additional information. Only return the results in the following JSON format:
#         Also kindly note, give cleaned values, there should not be \ or junk chars inside it. 
#         Return the JSON in a compact format without any extra spaces or newlines.

#         {{
#             "keywords": ["keyword1", "keyword2", ...],
#             "topics": ["automobile", "IT", "AI",...]
#         }}

#         Text: {transcription}
#     """
        
#     keywords_topics_res = run_ollama_prompt(extract_kwrds_prompt, llm_model)
#     keywords_topics_res = keywords_topics_res.replace("\n", "").replace(" ", "")
#     print("Extracted keywords and topics:", keywords_topics_res)

#     # convert into json format
#     try:
#         keywords_topics_dict = json.loads(keywords_topics_res)
#         #print('JSON Response:', keywords_topics_dict)
#     except json.JSONDecodeError as e:
#         print("Error decoding JSON:", e)
#         keywords_topics_dict = {"keywords": [], "topics": []}

#     return keywords_topics_dict

# def extract_brands_and_locations(transcription, llm_model):
#     print("=" * 100)
#     print("Extracting brands and locations...")

#     extract_brands_locations_prompt = f"""
#         From the following text, extract and return the following two categories of information:
#         1. Brands: Names of companies, manufacturers, or organizations (e.g., NVIDIA, Microsoft, Google, Toyota).
#         2. Locations: Physical or functional places (e.g., factory, datacenter, workstation).

#         Do not give any explanations or additional information. Only return the results in the following JSON format:
#         Also kindly note, give cleaned values, there should not be \ or junk chars inside it. 
#         Return the JSON in a compact format without any extra spaces or newlines.

#         {{
#             "brands": ["brand1", "brand2", ...],
#             "locations": ["location1", "location2", ...]
#         }}

#         Text: {transcription}
#         """

#     brands_locations_res = run_ollama_prompt(extract_brands_locations_prompt, llm_model)

#     # Preprocess the response to remove unwanted characters
#     brands_locations_res = brands_locations_res.replace("\n", "").replace(" ", "")

#     print("Extracted brands and locations:", brands_locations_res)

#     # Convert the response string to a dictionary
#     try:
#         brands_locations_dict = json.loads(brands_locations_res)
#     except json.JSONDecodeError as e:
#         print("Error decoding JSON:", e)
#         brands_locations_dict = {"brands": [], "locations": []}

#     return brands_locations_dict

# def summarize_transcription(transcription, llm_model):
#     print("=" * 100)
#     print("Summarizing transcription...")
#     summarization_prompt = f"""
#     Summarize the following text in a short and clear manner as simple paragraph. Return only the summarized text 
#     without any explanations or additional information, Nothing else.: {transcription}
    
#     summary:"""
#     summarized_transcription = run_ollama_prompt(summarization_prompt, llm_model)
#     print("Summarized Text:", summarized_transcription)
#     return summarized_transcription

# def find_sentiments(transcription, llm_model):
#     print("=" * 100)
#     print("Finding sentiments...")
#     sentiment_prompt = f"Please analyze the sentiment (positive, negative, neutral) of the following text:\n{transcription}. Also note we need single word answer either positive or negative or neutral. Important is do not give any explaination\n\nSentiment:"
#     sentiment = run_ollama_prompt(sentiment_prompt, llm_model)
#     print("Sentiment:", sentiment)
#     return sentiment

# transcription = """Generative AI refers to a category of artificial intelligence 
# systems designed to create new content, such as text, images, music, or even videos that 
# mimics or is inspired by existing data. These systems learn patterns, styles, 
# and structures from large datasets and use that knowledge to generate original outputs. 
# Unlike traditional AI, which might focus on analyzing or classifying data, generative AI is about producing something new.
# Pume is good brand from America, Mahindra is best Automotive from India
# """
# extract_keywords(transcription,llm_model)
# # extract_brands_and_locations(transcription,llm_model)
# # summarize_transcription(transcription,llm_model)
# # find_sentiments(transcription,llm_model)
