class Personagem:
    def __init__(self, nome, genero, altura, cor_cabelo, habilidades):
        self.nome = nome
        self.genero = genero
        self.altura = altura
        self.cor_cabelo = cor_cabelo
        self.habilidades = habilidades

    def apresentar_nome(self):
        print(f"Olá! Meu nome é {self.nome}.")

    def apresentar_genero(self):
        print(f"Meu genero e {self.genero}.")

    def apresentar_altura(self):
        print(f"Eu tenho {self.altura} de altura.")

    def apresentar_cabelo(self):
        print(f"Meu cabelo é da cor {self.cor_cabelo}.")

    def apresentar_habilidades(self):
        print(f"Minha habilidade é {self.habilidades}.")

