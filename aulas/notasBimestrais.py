if __name__ == '__main__':
    a_str = input("Digite a primeira nota: ")
    b_str = input("Digite a segunda nota: ")
    c_str = input("Digite a terceira  nota: ")
    d_str = input("Digite a quarta nota: ")
    a_int = int(a_str)  # converte string/texto para inteiro
    b_int = int(b_str)  # converte string/texto para inteiro
    c_int = int(c_str)
    d_int = int(d_str)

    media = (a_int + b_int + c_int + d_int)/4
    print(f'A média é: {media}')

    # https://panda.ime.usp.br/runestone/books/published/pensamentos/03-Pensamento-comunicacao/10-Exercicio-comentado.html
