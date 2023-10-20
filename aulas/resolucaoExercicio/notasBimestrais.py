def notas_bimestrais():
    a_str = input("Digite a primeira nota: ")
    b_str = input("Digite a segunda nota: ")
    c_str = input("Digite a terceira  nota: ")
    d_str = input("Digite a quarta nota: ")
    a_int = int(a_str)
    b_int = int(b_str)
    c_int = int(c_str)
    d_int = int(d_str)

    media = (a_int + b_int + c_int + d_int)/4
    return media
    #print(f'A média é: {media}')

