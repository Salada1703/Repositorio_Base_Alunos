class Midia:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

class Musica(Midia):
    def __repr__(self):
        return f"'{self.titulo}' por {self.artista}"
    
class Playlist:
    def __init__(self, nome: str, musicas: list [Musica]):
        self.nome = nome
        self.musicas = musicas

    def tocar_todas(self):
        print(f"\n Tocando a playlist '{self.nome}':")
        for musica in self.musicas:
            print(f" Tocando agora: {musica}")

musica_1=Musica ("Balanca e bafora", "GP DA ZL") 
musica_2= Musica ("sobe na moto roubadona ", "DJ kevinho da zs")
musica_3 = Musica ("5 da manha", "Natanzinho lima")
daylist= Playlist("Sua playlist diária",
                [musica_1, musica_2, musica_3])
daylist.tocar_todas()
print(musica_1)