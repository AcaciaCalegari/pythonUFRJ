#lista06-MT
#114153997
#Acacia Calegari

#1-
#nem tentei ainda


#2-
#acertei tudo
def faltas(f):
    """funcao q recebe as faltas dos times e
        retorna o total d faltas no campeonato"""
    total = sum(f[0][2] + f[1][2] + f[2][2])
    return  total


#3-
#acertei td
def insere(lista_numero, n):
    """funcao q dada uma lista ordenada crescente, e um numero inteiro n,
    inclui esse numero n na lista d maneira ordenada"""
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    return lista_numero

#4-
#acertei 6 , errei 4
def maiores(lista, n):
    """funcao q dada uma lista de numeros e um num inteiro n , retorna outra 
    lista q contem todos os numeros maiores que o numero inteiro inserido"""
    numeros = [lista for lista in lista if lista > n]
    return numeros

#5-
#acrertei tudo
def acima_da_media(*notas):
    """funcao q recebe uma lista com notas dos alunos d uma turma, e retorna
    a média dos alunos da turma e uma lista ordenada com as notas que
    ficaram acima da media"""
    media = sum(notas[0])//len(notas[0])
    nota_maior=[]
    for maior in notas[0]:
        if maior > media:
            nota_maior.append(maior)
    return sorted(nota_maior)

#6-
#acertei td
def eh_ordenada(l):
    """funcao q dada uma lista contendo uma quantdade qlq d valores, retorna se
    ela esta ordenada em crescente, decrescente ou desordenada, numa tupla
    cujo primeiro elemento eh True or False"""
    lista= l.copy()
    if l == sorted (lista):
        return  True , "crescente"
    elif l == sorted (lista,reverse=True):
        return True , "decrescente"
    else:
        return False , "desordenada"
























