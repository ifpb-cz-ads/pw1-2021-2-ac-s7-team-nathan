L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
m = int(input("Digite o valor a procurar:"))
x = 0
valida=0
valida2=0
entro=0
entro2=0
while x < len(L):
    if L[x] == p and valida2 !=1:
        print("%d achado primeiro na posição %d" % (p, x))
        valida=1
        entro=1
    if L[x] == m  and valida !=1:
        print("%d achado primeiro na posição %d" % (m, x))
        valida2=1
        entro2 = 1
    if L[x] == p and valida !=1:
        print("%d achado na posição %d" % (p, x))
        entro = 1
    if L[x] == m and valida2 !=1:
        print("%d achado na posição %d" % (m, x))
        entro2 = 1
    x += 1
if entro != 1:
    print("%d não encontrado" % p)
if entro2 != 1:
    print("%d não encontrado" % m)
