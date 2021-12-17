t = [-10, -8, 0, 1, 2, 5, -2, -4]
y=len(t)
x=0
soma=0
maior=t[0]
menor=t[0]
while x < y:
    if maior < t[x]:
        maior=t[x]
    if menor > t[x]:
        menor=t[x]
    soma=soma+t[x]
    x=x+1
media=soma/y
print("A media é igual a %d a maior temperatura é igual a %d e a menor igual a %d" % (media,maior,menor))