def listaXY(x,y):
    if x > y:
        return list(range(x,y-1,-1))
    else:
        return list(range(x,y+1))



def f(lista1):
    if len(lista1) >2:
        lista2 = lista1
    else:
        lista2 = lista1[:]
    list.append(lista1,[3,4])
    list.extend(lista1, [4,5])
    del lista1[2]
    if lista1[0] == 1:
        lista1 = lista1*2
    return lista2
