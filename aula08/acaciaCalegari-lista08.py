#lista08
#114153997
#AcaciaCalegari

from math import *

#1-

#a-
def somaSerie(n):
    '''funcao q dado n, calcula a soma da serie ate o termo n'''
    somaTotal = 0
    for i in range(n):
        serie = (pow(-1,i))/(2*i+1)
        somaTotal += serie
    return somaTotal
    

#b-
def SerieErro():
    '''funcao q que calcule a soma da serie com erro inferior
    a 0, 01, e retornara uma tupla com os dois valores calculados.'''
    n = 0
    soma = somaSerie(n)
    erro = fabs(soma - pi/4)
    while erro > 0.01:
        n += 1
        soma = somaSerie(n)
        erro = fabs(soma-pi/4)       
    return soma,n


#2-
def contato2(contatos,nome):
    """funcao q recebe como entrada a lista de contatos e uma string
    referente ao nome buscado, e retorna uma lista
    de contatos que contem o nome buscado."""

    
    ContatoBuscado = []

    for i in list(range(len(contatos))):
        if str.lower(nome) in str.lower(str(contatos[i][0])):
            ContatoBuscado.append(contatos[i])

    return ContatoBuscado
