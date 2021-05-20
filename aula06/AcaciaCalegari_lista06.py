#lista06
#114153997
#Acacia Calegari

#1-
#a-
def contatinhosApp(nome,tel,email,insta):
    '''funcao que receeb e retorna uma lista com as seguintes informacoes:
    nome, telefone, email e instagram'''
    cntt=[]
    list.insert(cntt,0,nome)
    list.insert(cntt,1,[tel])
    list.insert(cntt,2,email)
    list.insert(cntt,3,insta)
    return cntt


#b-
def atualizarContato(info,indice,novainfo):
    '''funcao que adiciona ou modifica informacao de um contato existente
    e retorna um valor booleano, indicando se houve ou nao alteracao.'''
    if indice == 0:
        list.insert(info,0,novainfo)
        return True
    elif indice == 1:
        list.insert(info,1,novainfo)
        return True
    elif indice == 2:
        list.insert(info,2,novainfo)
        return True
    elif indice == 3:
        list.insert(info,3,novainfo)
        return True
    else:
        return False

        
        
    
