try:
    arquivo=open("numeros.txt","w")
    for linha in range(1,100):
        arquivo.write("%d guilherme\n"% linha)
    arquivo.close()
except FileNotFoundError:
    print('arquivo nao encontrado')