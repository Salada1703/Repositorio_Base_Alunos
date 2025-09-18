estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50]
}
produto =input("digite o produto:")
venda=[[produto,int(input("digite a quantidade:"))]]
total = 0
print("Vendas:\n")
if produto in estoque:
  for operação in venda:
      produto, quantidade = operação
      preço = estoque[produto][1]
      custo = preço * quantidade
      print("%12s: %3d x %6.2f = %6.2f" %
            (produto, quantidade, preço, custo))
      estoque[produto][0] -= quantidade
      total += custo
else:
    print("insuficiente")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
