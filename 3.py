x=0
entre=1
list1=[0]
list2=[0]
y=0
while x != 0 or entre == 1:
    entre=0
    list1.append(int(input("Digite um numero no array 1")))
    list2.append(int(input("Digite um numero no array 2")))
    x=int(input("Digite 0 para sair e 1 se deseja contnuar adicionando numeros"))
    y=y+1
list1.pop(0)
list2.pop(0)
list3=[0]
x=0
while x < y or x < y:
    el1=list1[x]
    el2=list2[x]
    contador1=list3.count(el1)
    contador2=list3.count(el2)
    if contador1 < 1:
        list3.append(list1[x])
    if contador2 < 1:
        list3.append(list2[x])
    x=x+1
list3.pop(0)
x=0
for x in list3:
    print(x)

