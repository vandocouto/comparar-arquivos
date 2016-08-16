#!/usr/bin/python

def compara(original,copia):
    # arquivo original
    lista1=[]
    arquivo = open(original, 'r')
    for i in (arquivo.read().split()):
        lista1.append(i)
    # arquivo copia
    lista2=[]
    arquivo = open(copia, 'r')
    for i in (arquivo.read().split()):
        lista2.append(i)
    
    # comparando os arquivos
    return set(lista1) & set(lista2)

# retornando os valores repeditos
for i in compara("lista1","lista2"):
    print i
