class Pássaro():
    def __init__(self, tamanho, cores, espécie, sexo,habitat):
        self.tamanho = tamanho
        self.cores = cores
        self.espécie = espécie
        self.sexo = sexo
        self.habitat= habitat

    def cantar(self):
        return print(f'Sou um {self.espécie} cantando uma bela canção')

    def voar(self):
        return print('Batendo as asas e: voando... longe do meu {self.habitat}')
        
pássaro1 = Pássaro(0.14, ['Marrom', 'Branco', 'Cinza'], 'Pardal', 'M','city')
pássaro1.cantar()

pássaro2 = Pássaro(0.54, ['preto'], 'corvo', 'M','plantacoes')
pássaro2.cantar()

pássaro3 = Pássaro(0.79, ['vermelho', 'azul', 'amarelo','verde'], 'Arara', 'F','amazonia')
pássaro3.cantar()

pássaro4 = Pássaro(0.32, ['cinza','branco'], 'pombo de rodoviaria', 'M','rodoviaria')
pássaro4.cantar()














