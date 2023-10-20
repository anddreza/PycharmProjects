def alo_mundo():
    msg = "Alo mundo"
    #print(mensagem)
    return msg
def numero_informado():
    num = input("Informe um numero")
    #print("O numero informado foi: ", num)
    return num

def dois_numeros():
    a_str = input("Digite o primeiro numero: ")
    b_str = input("Digite o segundo numero: ")
    a_int = int(a_str)
    b_int = int(b_str)
    soma = a_int + b_int
    #print(f'A soma de {a_int} + {b_int} é: {soma}')
    return soma
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

def metros_centrimetros():
    a_str = input("Digite os metros: ")
    a_int = int(a_str)
    cent = a_int * 100
    #print(f'Os centimetros são: {cent}')
    return cent

def area_circulo():
    a_str = input("Digite a área do circulo: ")
    a_int = int(a_str)
    PI = 3,14
    area = PI * (a_int * a_int)
    #print("O valor da área circulo é ", area)
    return area