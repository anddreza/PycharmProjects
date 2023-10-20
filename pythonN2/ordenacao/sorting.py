# Vídeo "Quick Sort": https://youtu.be/wx5juM9bbFo
def quicksort(lista, inicio=0, fim=None):
    #Se fim for is None
    if fim is None:
        #O fim é o tamanho da lista -1, aquele indice será como pivô
        fim = len(lista)-1
        #Se inicio for menor que o fim
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:
            #troca de valores entre variaveis
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i