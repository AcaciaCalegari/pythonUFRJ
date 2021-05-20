#lista09
#114153997
#acacia calegari

#1-
def matrizMult(matriz, n):
    '''funcao que calcula e retorna a matriz resultante da
    multiplicacao de uma matriz por um numero.'''
    resultado = []
    for i in range(len(matriz)):
        multiplicacao = []
        for j in matriz[i]:
            num = j * n
            multiplicacao.append(num)
        resultado.append(multiplicacao)
    return resultado


#2-
def quemLig(n,contatos):
    '''funcao q retorne a lista com os dados do contatinho que tem aquele
    numero, ou retorne uma lista vazia, caso o numero nao esteja na agenda'''
    contatim = []
    for contato in contato2:
        for telefone in contato[1]:
            if n in telefone and contato not in contatim:
                contatim.append(contato)

    return contatim
