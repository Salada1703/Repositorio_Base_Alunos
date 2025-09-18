numeros=[1,3,5,7,10,23,32,33,44,55]
coordenadas=[1.6325,4.18976,6.75375]
motos=["bmw","honda","tigger","ducatti","kawasaki","yamaha","Shineray","Triumph","start","fan"]
print(numeros[5])
print(coordenadas[-2])
print(motos[8])

numeros.insert(4,7)
print(numeros)

numeros.pop(3)
print(numeros)

import random
cesta=["bmw","honda","tigger","ducatti","kawasaki","yamaha","Shineray","Triumph","start","fan"]
print(random.choice(cesta))