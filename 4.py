lista = [2]
p1 = 0
p2 = 0
lista = input("Digite os parenteses")
x = len(lista) - 1
while x >= 0:
    parentese = lista.reverse()
    if parentese == '(':
        p1 = p1 + 1
    elif parentese == ')':
        p2 = p2 + 1
    x = x - 1
if p1 == p2:
    print("OK")
else:
    print("ERROR")