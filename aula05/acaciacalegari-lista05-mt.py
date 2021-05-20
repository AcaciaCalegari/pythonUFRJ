#lista05 mt
#Acacia Calegari
#114153997

#1-
def num_palavra(frase):
    '''Funcao que dada uma frase,retorna o numero de palavras da frase.'''
    a = str.split(frase,' ')
    b = len(a)
    if a[0] == '':
        b -=1
    if a[len(a)-1] == '':
        b -=1
    return b        

#2-
def num_frase(frase):
    '''Funcao que conta o numero de frases que aparecem em um texto. Cada
        frase termina com um ponto final, exclamacao, interrogacao ou
        retircencias.'''
    '.' != '...'
    ponto = str.count(frase,'.',0)
    exclamacao = str.count(frase,'!',0)
    interrogacao = str.count(frase, '?', 0)
    reticencias = str.count(frase, '...',0)
    
    return ponto + exclamacao + interrogacao + -2* reticencias


#3-
def listas(l1,l2):
    '''funcao que intercala os elementos de duas listas l1, e l2.'''
    return [l1[0]]+[l2[0]]+[l1[1]]+[l2[1]]+[l1[2]]+[l2[2]]


#4-
def substitui_espaco(frase):
    '''funcao qe subistitui caracter de pontuacao por espaco'''
    '.' != '...'
    a= str.replace(frase,'-',' ')
    b= str.replace(a,',',' ')
    c= str.replace(b,':',' ')
    d= str.replace(c,';',' ')
    e= str.replace(d,'?',' ')
    f= str.replace(e,'!',' ')
    g= str.replace(f,'.',' ')
    h= str.replace(g,'...',' ')
    k= h
    return k

#5-
def invertida(frase):
    '''funcao q retorna a frase dada de forma inevrtida, sem letra maiuscula,
    e sem a pontuacao'''
    '.' != '...'
    a= str.replace(frase,'-',' ')
    b= str.replace(a,',',' ')
    c= str.replace(b,':',' ')
    d= str.replace(c,';',' ')
    e= str.replace(d,'?',' ')
    f= str.replace(e,'!',' ')
    g= str.replace(f,'.',' ')
    h= str.replace(g,'...',' ')
    k= h
    invercao = k
    f= str.split(invercao)
    return str.lower(str.join(' ',f[::-1]))


#6-
def piramide(a,b):
    '''funcao que constroi uma piramide de numeros inteiros, dados dois
    numeros'''
    if a == b:
        return [a]
    elif a > b:
        c= list(range(a,b-1,-1))
        d= c[-2::-1]
        return c+d
    elif a < b:
        e= list(range(a,b+1))
        f= e[-2::-1]
        return e+f

#7
def colchao(m,h,l):
    '''funcao que retorna True se o colchao passar pela porta, e False, caso
    contrario'''
    m.sort()
    if m[0] > h:
        if m[0] > l:
            return False
        elif m[1] > l:
            return False
        else:
            return True
    elif m[1] > h:
        return False
    else:
        return True




    











    































    
    














    

