def listas():
    L=[8,9,15,17,3,7,9,8,2,38]
    for guilherme in L:
        print(guilherme)
print("----x-------")
def marcas():
    L=["nike", "adidas", "puma"]
    for s in L:
        for letra in s:
            print(letra)
print("------x-------")
def maior():
    L=[1,-7,2,4,12,34,65,14,13,-65]
    maximo=L[0]
    for e in L:
        if e> maximo:
            maximo=e
    print(maximo)    
print("----x-----")
def menor():
    L=[1,-7,2,4,12,34,65,14,13,-65]
    minimo=L[0]
    for e in L:
        if e< minimo:
            minimo=e
    print(minimo)
print("------x-------")
for v in range(5,8):
    print(v)
print("-----x-----")
for t in range(3,33,3):
    print(t, end=" ")
print("-------x--------")
nome="Guilherme"
idade=15
grana=3.600
print("%-20s tem %010d anos e R$%5.3f no bolso." % (nome,idade,grana))
