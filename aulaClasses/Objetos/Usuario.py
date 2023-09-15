class Usuario:
    # Se quisesse já criar um objeto com o nome e idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__update = 1

    @property
    def nome(self): # equivalente ao get
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome
        self.__update += 1

    def boas_vindas(self):
        print("Bem vindo " + self.nome)