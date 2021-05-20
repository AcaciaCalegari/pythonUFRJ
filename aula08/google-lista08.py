def filtrasoma(val,n):
    soma=0
    for valor in val:
        if valor>n:
            soma = soma+valor
    return soma


def filtrasoma1(valores,n):
    soma = 0
    i=0
    while i<len(valores):
        if valores[i]>n:
            soma=soma+valores[i]
        i=i+1
    return soma



def filtrasoma2(valores,n):
    soma=0
    i=0
    while i<len(valores):
        if valores[i]>n:
            i=i+1
            soma=soma+valores[i]
    return soma



def filtrasoma3(valores,n):
    soma=0
    i=0
    while i<len(valores):
        if valores[i]>n:
            i=i+1
        soma=soma+valores[i]
    return somas


def filtrasoma4(valores,n):
    soma=0
    i=0
    while i<len(valores):
        if valores[i]>n:
            soma=soma+valores[i]
    return soma


def efe(n):
    lista=[]
    for i in range(0,11):
        list.append(lista,i*n)
    return lista







def F(c1,c2):
    c3=[]
    for i in c1:
        if i in c2:
            list.append(c3,i)
    return c3







def F2(l):
    s=0
    for e in l[::2]:
        s += e
    return s





def ocorrencia1(frase,letra):
    i=0
    while i<len(frase):
        if frase[i] == letra:
            pos=i
        i = i+1
    return pos


def ocorrencia2(frase,letra):
    for i in range(len(frase)):
        if frase[i] == letra:
            pos=i
    return pos








    
            












