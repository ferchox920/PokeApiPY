import requests
import matplotlib.pyplot as plt
from PIL import Image

pokemon = input("Introduce el nombre o número del pokemon: ")
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
res = requests.get(url)

if res.status_code != 200:
    print("No se encontró ningún pokemon con ese nombre o número")
    exit()

imagen = Image.open(requests.get(res.json()['sprites']['front_default'], stream=True).raw)
plt.title(res.json()['name'])
impgplot = plt.imshow(imagen)
plt.show()
