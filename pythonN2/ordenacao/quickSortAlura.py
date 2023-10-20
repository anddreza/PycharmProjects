from array import array

def importa_lista(arquivo):
    lista = []
    with open(arquivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
        lista.append(line)
    return lista

def ordena(lista):
    tamanho_da_lista = len(lista)
    if tamanho_da_lista > 0:
        quick_sort(lista, 0, tamanho_da_lista - 1)

def quick_sort(lista, inicio, fim):
    if inicio > fim:
        return
    anterior = inicio
    posterior = fim
    pivo = lista[inicio]

    while anterior < posterior:
        while anterior < posterior and lista[posterior] > pivo:
            posterior = posterior - 1

        if anterior < posterior:
            lista[anterior] = lista[posterior]
            anterior = anterior + 1

        while anterior < posterior and lista[anterior] <= pivo:
            anterior = anterior + 1

        if anterior < posterior:
            lista[posterior] = lista[anterior]
            posterior = posterior - 1

        lista[anterior] = pivo

    quick_sort(lista, inicio, anterior - 1)
    quick_sort(lista, anterior + 1, fim)

def main():
    lista_de_alunos = importa_lista('../data/lista_alunos')

    ordena(lista_de_alunos)

    for nome in lista_de_alunos:
        print(nome)

if __name__ == "__main__":
    main()