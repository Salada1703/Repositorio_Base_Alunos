tupla=("a","b","c")
tupla
#print(tupla)
print("----x------")
tupla=100,200,300
tupla
#print(tupla)
print("-----x------")
L = [5,10,15,20,25,20,35,40,45,50]
print("--- divisao ---")
for x, e in enumerate(L):
    print("%d / %d =%f"%(x,e,x/e))
print("--- soma ---")
for x, e in enumerate(L):
    print("%d + %d =%d"%(x,e,x+e))  
print("--- subtracao ----")
for x, e in enumerate(L):
    print("%d - %d =%d"%(x,e,x-e))
print("--- mutiplicacao ---")
for x, e in enumerate(L):
    print("%d X %d =%d"%(x,e,x*e))      