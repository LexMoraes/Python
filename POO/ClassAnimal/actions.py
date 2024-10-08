from model import Animal, Catioro, Gato, Passaro


class AnimalActions(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def teste(self):
        if self.especie == "Catioro".lower():
            catioro = Catioro(especie=self.especie)
            catioro.emitir_som()

        elif self.especie == "Gato".lower():
            gato = Gato(especie=self.especie)
            gato.emitir_som()

        elif self.especie == "Passaro".lower():
            passaro = Passaro(especie=self.especie)
            passaro.emitir_som()

