##Retirado do site:
##https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OQuickSort.html
import random

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def geraNumero():
    vet1 = []
    print("\nAleatorio:\n")
    #for i in range(10000)
    for i in range(1,100):
        #vet1.append(i)
        vet1[i].append(random.randint(1, 10000))
    print(vet1)
    quickSortHelper(vet1, 0, len(vet1) - 1)
    print(vet1)


def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

##alist = {}
#quickSort()
##print(alist)
