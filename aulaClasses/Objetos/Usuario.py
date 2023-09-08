class Usuario:
    # Se quisesse já criar um objeto com o nome e idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def boas_vindas(self):
        print("Bem vindo " + self.nome)