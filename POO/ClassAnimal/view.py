from actions import AnimalActions
from model import Animal



class Menu:
    def __init__(self):
        self._name = None

    def mostrarMenu(self):

        self._name = self.set_animal()

        while self._name != 0:
            animal = Animal(self._name)
            teste = AnimalActions(self._name)
            teste.teste()
            self._name = self.set_animal()

    def set_animal(self) -> str:
        print("Esse é um teste para verificar o som do animal.")
        name = input("Informe o nome do animal: ")
        return name


