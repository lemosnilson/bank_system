class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = 001

    # O método estático "código do banco" poderia, também, simplesmente ser:
    # código_banco = 001c
    # que, nesse caso, é um ATRIBUTO estático, pois não usao SELF (não cria objeto e nem utiliza o __init__.
    # Muito mais simples.

    def extrato(self):
        print("Saldo de {} do titular {}.".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __saque_permitido(self, valor):
        disponivel = (self.__saldo + self.__limite)
        return valor <= disponivel

    def sacar(self, valor):
        if (self.__saque_permitido(valor)):
            self.__saldo -= valor
        else:
            print("Impossível sacar o valor de {}. Saldo insuficiente.".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}