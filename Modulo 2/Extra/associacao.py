class Pessoa:
    def __init__(self, nome, diciplina):
        self.nome=nome
        self.diciplina=diciplina

class SalaDeAula:
    def __init__(self, numero: int, capacidade: int):
        self.numero = numero
        self.capacidade = capacidade
        print(f"Sala {self.numero} está disponível.")
class Professor (Pessoa):
    def dar_aula(self, sala: SalaDeAula):
        print(f"O Prof. {self.nome} de {self.diciplina} está dando aula na sala {sala.numero}.")

sala1=SalaDeAula(101,30)

pessoa=Professor("Guilherme", "ed.fisica")
pessoa.dar_aula(sala1)







