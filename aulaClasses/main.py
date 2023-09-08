class Usuario:
    # Se quisesse já criar um objeto com o nome e idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

if __name__ == '__main__':
    user = Usuario("Andreza", 27)
    #user.nome = "Andreza"
    #user.idade = 27

    print("Nome" + user.nome + " , idade " + str(user.idade))
    print(f"Nome: {user.nome}, idade: {user.idade}")

