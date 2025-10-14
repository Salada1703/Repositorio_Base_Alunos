from classe_animal import Animal
from classe_passaro import Pássaro
from classes_ex_01 import AnimaisMarinhos

x = "Olá, Mundo!"
# print(len(x))
minha_tupla = ("Maçã", "Banana", "Cereja")
# print(len(minha_tupla))
este_dicionário = {
    "marca": "Chevrolet", 
    "modelo": "Opala",
    "ano": 1969
}
# print(len(este_dicionário))

animal1 = Animal("scooby-doo", "dogue alemão")
animaismarinhos1 = AnimaisMarinhos("sim", "peixe-palhaço","Nemo", "corais", 0.03)
passaro1 = Pássaro(0.74, "azul","arara","M", "amazonia")

def comunicar(qualquer_animal):
    print(f"tentando comunicacao {qualquer_animal.espécie}")
    qualquer_animal.fazer_som()

print("-"*50)
comunicar(animal1)

print("-"*50)
comunicar(animaismarinhos1)

print("-"*50)
comunicar(passaro1)