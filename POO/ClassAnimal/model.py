'''Questão 1'''

class Pessoa:
    def __init__(self, name, idade):
        self._name = name
        self._idade = idade

    def mostrar_informacoes(self):
        print(f"Seu nome é {self._name} e você tem {self._idade} anos.")

'''Questão 2'''

class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor
        return f'valor depositado: ', self.valor

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            return f'valor sacado:', self.saldo
        else:
            print(f'Não foi possível realizar o saque: {valor} é maior que saldo em conta.')

    def mostrar_saldo(self):
        return f'Seu saldo é: ', self.saldo

'''Questão 3'''

class Animal:
    def __init__(self, especie):
        self.especie = especie

    def emitir_som(self):
        print("Emitindo som...")

    def mover(self):
        print("Movendo-se...")



class Gato(Animal):
    def emitir_som(self):
        print("Gato miando...")

    def mover(self):
        print("Gato pulando...")

class Catioro(Animal):
    def emitir_som(self):
        print("Catioro latindo...")

    def mover(self):
        print("Catioro correndo...")

class Passaro(Animal):
    def emitir_som(self):
        print("Passaro cantando...")

    def mover(self):
        print("Passaro voando...")


'''Questão 4'''

class Carro:
    def __init__(self, _marca, _modelo, _ano):
        self._marca = None
        self._modelo = None
        self._ano = None

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_ano(self):
        return self._ano

    def set_ano(self, ano):
        self._ano = ano