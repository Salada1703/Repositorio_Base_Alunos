class Pessoa:
    def __init__(self, nome, idade, altura, peso, cpf, email, telefone, endereco, cidade, pais, profissao, nacionalidade, cor_cabelo, cor_olhos, personalidade, hobby):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        self._peso = peso
        self.__cpf = cpf
        self._email = email
        self._telefone = telefone
        self.__endereco = endereco
        self._cidade = cidade
        self._pais = pais
        self._profissao = profissao
        self._nacionalidade = nacionalidade
        self._cor_cabelo = cor_cabelo
        self._cor_olhos = cor_olhos
        self._personalidade = personalidade
        self._hobby = hobby

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def altura(self):
        return self._altura

    @property
    def peso(self):
        return self._peso

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self._email

    @property
    def telefone(self):
        return self._telefone

    @property
    def endereco(self):
        return self.__endereco

    @property
    def cidade(self):
        return self._cidade

    @property
    def pais(self):
        return self._pais

    @property
    def profissao(self):
        return self._profissao

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @property
    def cor_cabelo(self):
        return self._cor_cabelo

    @property
    def cor_olhos(self):
        return self._cor_olhos

    @property
    def personalidade(self):
        return self._personalidade

    @property
    def hobby(self):
        return self._hobby

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    @peso.setter
    def peso(self, valor):
        self._peso = valor

    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    @email.setter
    def email(self, valor):
        self._email = valor

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @endereco.setter
    def endereco(self, valor):
        self.__endereco = valor

    @cidade.setter
    def cidade(self, valor):
        self._cidade = valor

    @pais.setter
    def pais(self, valor):
        self._pais = valor

    @profissao.setter
    def profissao(self, valor):
        self._profissao = valor

    @nacionalidade.setter
    def nacionalidade(self, valor):
        self._nacionalidade = valor

    @cor_cabelo.setter
    def cor_cabelo(self, valor):
        self._cor_cabelo = valor

    @cor_olhos.setter
    def cor_olhos(self, valor):
        self._cor_olhos = valor

    @personalidade.setter
    def personalidade(self, valor):
        self._personalidade = valor

    @hobby.setter
    def hobby(self, valor):
        self._hobby = valor

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.")

    def trabalhar(self):
        print(f"{self.nome} está trabalhando como {self.profissao} agora.")

    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}.")

    def dormir(self, horas):
        print(f"{self.nome} dormiu por {horas} horas e está revigorado!")

    def praticar_hobby(self):
        print(f"{self.nome} está se divertindo com seu hobby favorito: {self.hobby}.")

    def envelhecer(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário! Agora tem {self.idade} anos.")

    def mudar_trabalho(self, nova_profissao):
        print(f"{self.nome} trocou de profissão! Agora trabalha como {nova_profissao}.")
        self.profissao = nova_profissao

    def falar(self, mensagem):
        print(f"{self.nome} diz: '{mensagem}'")

    def viajar(self, destino):
        print(f"{self.nome} está viajando para {destino}. Que aventura!")

    def exercitar(self):
        print(f"{self.nome} está se exercitando para manter a forma física.")
