
val=True
try:
    a=int(input("chiffre entier et paire de a: "))
    b=int(input("chiffre entier et paire de b: "))
except:
    val=False
    print("L'une des deux valeurs ne sont pas des entier")
try:
    assert a%2==0
except:
    val=False
    print("a doit être paire")
try:
    assert b!=0
except:
    val=False
    print("b ne peut pas valoir 0 car diviser par 0 est impossible")

if(val==True):
    print("La résultat de la division {}/{} = {}".format(a,b,a/b))
