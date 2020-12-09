import math

def add(a,b):
    return a+b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def sous(a,b):
    return a-b

x=int(input("saisir le premier chiffre: "))
y=int(input("saisir le deuxieme chiffre: "))
print("addition {}".format(add(x,y)))
print("mult {}".format(mult(x,y)))
print("div {}".format(div(x,y)))
print("sous {}".format(sous(x,y)))

