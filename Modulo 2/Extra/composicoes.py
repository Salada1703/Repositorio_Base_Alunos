class ItemDoPedido:
    def __init__(self, produto: str, quantidade: int, preco_unitario: float):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_subtotal(self) -> float: 
        return self.quantidade * self.preco_unitario


class Pedido: 
    def __init__(self, id_cliente: int):  
        self.id_cliente = id_cliente
        self._itens = []
        print(f"\nPedido criado para o cliente {self.id_cliente}.")

    def adicionar_item(self, produto: str, quantidade: int, preco_unitario: float):
        novo_item = ItemDoPedido(produto, quantidade, preco_unitario)
        self._itens.append(novo_item)
        print(f"Item '{produto}' adicionado ao pedido.")  

    def calcular_total(self):
        total = sum(item.calcular_subtotal() for item in self._itens)
        print(f"Total do Pedido: R${total:.2f}")


pedido_123 = Pedido(957)  

pedido_123.adicionar_item("Monitor", 1, 1250.00)
pedido_123.adicionar_item("Mouse Gamer", 1, 150.00)
pedido_123.adicionar_item("Teclado Gamer", 1, 350.00)
pedido_123.adicionar_item("Console", 1, 3000.00)
pedido_123.adicionar_item("Memória RAM", 1, 650.00)
pedido_123.calcular_total()
