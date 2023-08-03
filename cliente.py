class Cliente:

    def __init__(self, nome):
        self.nome = nome

    #abaixo o getter
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.nome.title()

    #abaixo o setter
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome