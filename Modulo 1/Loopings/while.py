def tabuada():
    n=int(input("digite um numero: "))
    x=1
    while x<=10:
        print(n,"x",x,"=",x*n)
        x=x+1
print("-----x------")

def breakand():
    s=0
    while True:
        v=int(input("digite um numero a somar ou 0 para sair:"))
        if v==0:
            break
        s=s+v
    print(s)
print("-------x-------")

    
