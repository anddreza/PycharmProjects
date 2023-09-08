class Usuario:
    def __init__(self):
        self.nome = ""
        self.idade = 0

if __name__ == '__main__':
    user = Usuario()
    user.nome = "Andreza"
    user.idade = 27
    print("Nome" + user.nome + " , idade " + str(user.idade))
    print(f"Nome: {user.nome}, idade: {user.idade}")