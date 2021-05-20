def g(x,y):
    acumula=0
    count=0
    for i in range(x):
        for j in range(i,y):
            count=count+1
            acumula = acumula + y
    print (count)
    return acumula


def m(x,y):
    acumula = 0
    for i in range(x):
        for j in range(y):
            acumula = acumula + y
    return acumula



def f(x,y):
    acumula = 0
    for i in range(x):
        for j in range(y):
            acumula = acumula + y
    return acumula




def f1(x,y):
    acumula1 = 0
    acumula2 = 0
    for i in range(x):
        for j in range(y):
            acumula2 = acumula2 + y
        acumula1 = acumula1 + acumula2
    return acumula1


def f2(x,y):
    acumula1 = 0
    for i in range(x):
        acumula2 = 0
        for j in range(y):
            acumula2 = acumula2 + y
        acumula1 = acumula1 + acumula2
    return acumula1






