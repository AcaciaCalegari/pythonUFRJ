#lista 07
#114153997
#Acacia Calegari

import random

#1-
def dados():
    """Funcao q simula conta quantas vezes os dados foram jogados ate sair numeros iguais."""
    cont = 0  
    while True:
        dado1 = [random.randint(1,6)]
        dado2 = [random.randint(1,6)]
        cont += 1
        if dado1 == dado2:
            return cont
    
#2-
def contato(contatos,nome):
    """Funcao q recebe uma lista e um nome, e retorna outra lista
        com todos os contatos que tem esse mesmo nome."""
    lista = []
    n = 0
    while n < (len(contatos)):
        copia = str.lower(contatos[n][0])
        if str.lower(nome) in copia:
            lista = lista + contatos[n]
        n += 1
    return lista
