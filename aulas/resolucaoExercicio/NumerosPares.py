
if __name__ == '__main__':
    lista_numero = []

    while(True):
        num = int(input())

        if num == 0:
            break

        lista_numero.append(num)

    soma_par = 0
    soma_par = 0
    cont_par = 0
    cont_impar = 0
    for n in lista_numero:
        if n % 2 == 0:
            soma_par += n
            cont_par += 1
        else:
            soma_par += n
            cont_impar += 1

    print("Qtde de numeros pares: " + str(cont_par))
    print("Soma de numeros pares" + str(soma_par))
    print("Qtde de numeros impares" + str(cont_impar))
    print("Media de numeros impares" +  str(soma_par / cont_impar))