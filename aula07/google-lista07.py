def primeira_vogal(palavra):
    i=0
    while i < len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            vogal = palavra [i]
            i = i +1
            return vogal








lista1 = list(range(5,25,5))
lista2 = lista1[:]
lista3 = lista2
# ponto 1
print('ponto1')
print(id(lista1))
print(id(lista2))
print(id(lista3))
 
lista1[1] = [[1,2]]
lista3[0:2] = [(1,2)]

# ponto 2
print('ponto2')
print(lista1)
print(lista2)
print(lista3)

 
lista1[1][0]= '12'
lista2[1:4] = '123'
# ponto 3

print('ponto3')
print(hex(id(lista1)))
print(hex(id(lista2)))
print(hex(id(lista3)))
 





