for x in range(11):
    print("9x{} = {}".format(x, x*9))

#Destructuration en tant que valeurs
a, b = (1, 2)
print(a)
# Prints: 1
print(b)
# Prints: 2


# Initialisation du jeu de cartes
jeu_de_cartes=["1","2","3","4","5","6","7","8","9","10","V","D","R"]
# On affiche le jeu de cartes
for carte in jeu_de_cartes:
    print (carte)
jeu_de_cartes.sort()
print (jeu_de_cartes)

#Conversion

devise = input("Devise : ")
montant = int (input ("Montant : "))

# 1 euro = 1.27 $

facteur_euro_dollar = 1.27

if devise == 'E' :
    print ("%f $" % (montant * facteur_euro_dollar))
elif devise == '$' :
    print ("%f Euros" % (montant / facteur_euro_dollar))
else :
    print ("Je n'ai rien compris") # affichage d'un message d'erreur

#exo3

fr_ang = {
  "langage": "language",
  "fille": "girl",
  "voiture": "car",
  "ciel": "sky",
  "fenetre": "window"
}

fr_ang['mot'] = "word"

print("my dictionnary (fr:ang) : \n", fr_ang.values())

to_del = [key for key in fr_ang if key.startswith('c')] 
for key in to_del: del fr_ang[key]

print("my dictionnary after supression (fr:ang) : \n", fr_ang.values())