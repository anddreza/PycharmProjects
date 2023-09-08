from Objetos.Usuario import Usuario

if __name__ == '__main__':
    user = Usuario("Andreza", 27)
    #user.nome = "Andreza"
    #user.idade = 27

    user_two = Usuario(idade=32, nome="Fernanda")

    print("Nome" + user.nome + " , idade " + str(user.idade))
    print(f"Nome: {user.nome}, idade: {user.idade}")

    user.boas_vindas()
    user_two.boas_vindas()
