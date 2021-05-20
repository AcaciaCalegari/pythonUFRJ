#lista08-MT
#acacia calegari
#114153997


#3-
#acertei td
def qtd_divisores(n):
    '''funcao q conta quants divisores um numero tem'''
    cont = 0 
    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1
    return cont 


#acertei 3, errei 7 pq esqci a funcao q arredonda
def soma_h(n):
    '''funcao q calcula e retorna o valor h com n termos, onde n eh
    inteiro e dado como entraada'''
    h = 0
    for i in range (1, n+1):
        j = 1/i
        h += (j)
    return h
