try:
    with open("test.txt",'r') as fic: #r pour "read"
        res=fic.read()
        print(res)
except FileNotFoundError:
    print("fichier introuvabe.")

try:
    with open("arriver.txt",'w') as fic:
        fic.write(res)
except FileNotFoundError:
    pirnt("fichier introuvable")
