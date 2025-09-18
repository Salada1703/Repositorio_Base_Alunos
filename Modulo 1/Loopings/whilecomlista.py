def whilecomlista():
    L=[]
    while True:
        n=(input("digite um numero(0sai):"))
        if n=="pare":
            break
        L.append(n)
    x=0
    while x <len(L):
        print(L[x])
        x=x+1
whilecomlista()