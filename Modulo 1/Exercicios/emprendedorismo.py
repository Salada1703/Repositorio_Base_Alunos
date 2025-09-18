estoque = {
    "Capacete esportivo": [10, 250.00],
    "Jaqueta de couro com proteção": [5, 399.90],
    "Luva com proteção térmica": [20, 89.99],
    "Bota para motociclismo": [8, 299.90],
    "Kit corrente-transmissão": [15, 150.00],
    "Óleo lubrificante para motor": [30, 35.00],
    "Pneu traseiro 150/60": [12, 450.00],
    "Pneu dianteiro 110/70": [10, 400.00],
    "Manopla esportiva": [25, 40.00],
    "Retrovisor universal": [18, 55.00],
    "Bateria selada 12V": [7, 220.00],
    "Baú traseiro 45L": [6, 310.00],
    "Protetor de motor (mata-cachorro)": [10, 180.00],
    "Capa de chuva para motoqueiro": [20, 70.00],
    "Lâmpada LED farol": [40, 25.00],
    "Freio a disco ventilado": [9, 150.00],
    "Escapamento esportivo": [5, 600.00],
    "Suporte para celular": [30, 35.00],
    "Pastilha de freio dianteira": [14, 45.00],
    "Câmera de ação para capacete": [3, 500.00]
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