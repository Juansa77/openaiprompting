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
Abrams ama a la franquicia, de eso no cabe duda. Por descontado, es un director imprevisible, errático en muchas ocasiones, y con dificultades a la hora de marcar el tempo de la acción, de manejar los acelerones y las demoras que requiere una trama como esta, desgajada en varias acciones paralelas que han de unirse en el tramo final. Bien, eso es más que sabido. Pero también es un cineasta apasionado, visceral. Y más allá de sus debilidades, "El ascenso de Skywalker", gracias a la apuesta de Abrams, se rodea de un cierto aire clásico, de una cierta idea de regreso a un terreno que nunca se debió abandonar. Se percibe en la elegancia y la precisión de sus imágenes y en la delicadeza con la que se muestra el retorno de algunos antiguos personajes (alguno de ellos, imprevisible).

Desde los gloriosos días de "La guerra de las galaxias" no se veía un "Star Wars" tan empapado de emotividad. El último tercio de “El ascenso de Skywalker” enternecerá al más reacio y Abrams se entrega a una vuelta a los orígenes sin engolar la voz, sin un solo aspaviento, con la alegría de un fan que puede jugar con sus personajes e iconos favoritos y que se puede permitir que regrese la legendaria nave Ala-Y de Luke Skywalker o realizar una excursión hasta las mismas entrañas de la Estrella de la Muerte (el duelo con espadas láser que mantienen en sus desvencijados restos Rey y Kyro se convierte en una de las mejores secuencias de las nueve entregas. Y su culminación, uno de los instantes más turbadores del cine reciente).
"""
prompt = f"""
extrae los sentimientos del texto y dime en una sola palabra si la crítica es positiva o negativa. Devuelve en un objeto json con sentimientos y valoración como claves
Review:```{text}```
"""


#USAMOS TRIPLES COMILLAS EN LA VARIABLE TEXTO PARA QUE EL MODELO ENTIENDA QUE ES UNA SECCIÓN SEPARADA
response = get_completion(prompt)
print(response)