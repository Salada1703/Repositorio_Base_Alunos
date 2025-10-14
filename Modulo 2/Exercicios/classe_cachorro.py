from Exercicios.classe_animal import Animal
from classes_ex_03 import Pessoa
from classe_gato import Gato

class Cachorro (Animal):
    def __init__(self,nome, raca):

        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        return print(f"{self.nome} está latindo: Au Au!")

    def abanar_rabo(self):
        return print(f"{self.nome} está abanando o rabo.")

cachorro1= Cachorro('Spike','Pitbull')
cachorro1.fazer_som()
cachorro1.abanar_rabo()

humano1= Pessoa('Guilherme',15,1.68,55,'Programador', 'brasileiro','preto','castanho','alegre','jogar bola')
humano1.apresentar()

gato=Gato('macumbinha')
gato.fazer_som()