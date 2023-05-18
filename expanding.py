import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key  = os.getenv("OPENAI_API_KEY")

#FUNCIÓN PARA VISUALIZAR LAS PROMPTS Y LAS RESPUESTAS




def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature= 0.7, # Cambiamos el valor de temperatura
    )
    return response.choices[0].message["content"]
# given the sentiment from the lesson on "inferring",
# and the original customer message, customize the email
sentiment = "negative"

review = f"""
Las tartas están buenísimas, pero el servicio es PÉSIMO. La cola llega al otro lado de la calle. Las dos chicas que atienden en la barra está claro que no valen para esto.... No las he visto más lentas. …Más
"""
prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service. 
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""


#USAMOS TRIPLES COMILLAS EN LA VARIABLE TEXTO PARA QUE EL MODELO ENTIENDA QUE ES UNA SECCIÓN SEPARADA
response = get_completion(prompt)
print(response)