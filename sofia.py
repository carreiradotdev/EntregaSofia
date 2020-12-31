from random import randint

def seq(a,b,c):     # Alinea a)
    lista = []
    for i in range(c):
        lista.append(randint(a,b))
    return lista

def rem(w):     # Alinea b)
    clean = []
    for lista in w:
        if len(lista) != 0 and counter(lista) != 1:
            clean.append(lista)
    return clean

def counter(lista):
    checker = []
    for item in lista:
        if item not in checker:
            checker.append(item)
    return len(checker)

def value(x):   # Alinea c)
    a = 0
    b = 0
    for item in x:
        if item % 2 == 0:
            a += item
        else:
            b += 1
    return(abs(2*(a)-b))

def rare(w):    # Alinea d)
    clean = []
    for lista in w:
        str1 = ""
        for item in lista:
            str1 += str(item)
        if "010" in str1:
            clean.append(lista)
    return clean



if __name__ == "__main__":
    armazem = []
    for i in range(1000):
        armazem.append(seq(randint(-9,0), randint(0,9), randint(0,10)))
    armazem = rem(armazem)
    print(value([-2,3,3,-1,-2]))
    print(value([1,1,1,1,0,2]))
    print(rare(armazem))
