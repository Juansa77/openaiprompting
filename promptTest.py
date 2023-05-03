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
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text = f"""
text value
"""
prompt = f"""
prompt
```{text}```
"""

#USAMOS TRIPLES COMILLAS EN LA VARIABLE TEXTO PARA QUE EL MODELO ENTIENDA QUE ES UNA SECCIÓN SEPARADA
response = get_completion(prompt)
print(response)