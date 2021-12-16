print("Digite pausadamente as letras")
x=1
list=[0]
while x !=0:
    list.append(input())
    x=int(input("Digite 0 para sair ou 1 para continuar"))
list.remove(0)
string="{ "
a=list.count("a")
if a > 0:
    string=string + "a:%d " % (a)
b=list.count("b")
if b > 0:
    string = string + "b:%d " % (b)
c=list.count("c")
if c > 0:
    string=string + "c:%d " % (c)
d=list.count("d")
if d > 0:
    string=string + "d:%d " % (d)
e=list.count("e")
if e > 0:
    string=string + "e:%d " % (e)
f=list.count("f")
if f > 0:
    string=string + "f:%d "  % (f)
g=list.count("g")
if g> 0:
    string=string + "g:%d " % (g)
h=list.count("h")
if h> 0:
    string=string + "h:%d " % (h)
i=list.count("i")
if i> 0:
    string=string + "i:%d " % (i)
j=list.count("j")
if j> 0:
    string=string + "j:%d " % (j)
k=list.count("k")
if k> 0:
    string=string + "k:%d " % (k)
l=list.count("l")
if l> 0:
    string=string + "l:%d " % (l)
m=list.count("m")
if m> 0:
    string=string + "m:%d " % (m)
n=list.count("n")
if n> 0:
    string=string + "n:%d " % (n)
o=list.count("o")
if o> 0:
    string = string + "o:%d " % (o)
p=list.count("p")
if p> 0:
    string=string + "p:%d " % (p)
q=list.count("q")
if q> 0:
    string=string + "q:%d " % (q)
r=list.count("r")
if r> 0:
    string=string + "r:%d " % (r)
s=list.count("s")
if s> 0:
    string=string + "s:%d " % (s)
t=list.count("t")
if t> 0:
    string=string + "t:%d " % (t)
u=list.count("u")
if u> 0:
    string=string + "u:%d " % (u)
w=list.count("w")
if w> 0:
    string=string + "w:%d " % (w)
x=list.count("x")
if x> 0:
    string=string + "x:%d " % (x)
y=list.count("y")
if y> 0:
    string=string + "y:%d " % (y)
z=list.count("z")
if z> 0:
    string=string + "z:%d " % (z)
ç=list.count("ç")
if ç> 1:
    string=string + "ç:%d " % (ç)
v=list.count("v")
if v> 1:
    string=string + "v:%d " % (v)
string=string+"}"
print(string)

