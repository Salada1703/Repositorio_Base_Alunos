class AnimaisMarinhos():
    def __init__(self, tem_escamas, espécie, nome, habitat, tamanho):
        self.tem_escamas = tem_escamas
        self.espécie = espécie
        self.nome = nome
        self.habitat = habitat
        self.tamanho = tamanho

    def viver_na_agua(self):
        return print(f'{self.nome} está vivendo pacificamente no {self.habitat}.')

    def nadar(self):
        return print(f'{self.nome} ({self.espécie}) está nadando alegremente!')

    def apresentar(self):
        escamas = 'tem escamas' if self.tem_escamas else 'não tem escamas'
        return print(f'Olá! Eu sou {self.nome}, um {self.especie} de {self.tamanho} metros e {escamas}.')

    def comer(self):
        return print(f'{self.nome} está se alimentando no {self.habitat}.')

    def dormir(self):
        return print(f'{self.nome} está descansando no {self.habitat} após um longo dia.')
    
    def fazer_som(self):
        return print("glupp, glupp...")
