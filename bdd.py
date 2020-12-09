from sqlite3 import*

#connection
connection = connect("base.db")#si la base n'existe pas, la base se créer elle-même
cursor= connection.cursor()
new_etudiant=(cursor.lastrowid, "Toto","Tata",25)
# '?' représente les valeur de la table (ici, le nom, prénom id et l'age)
cursor.execute('INSERT INTO etudiant VALUES(?,?,?,?)', new_etudiant)
connection.commit()
print("le nouvel utilisateur a été ajouté en BD")
cursor.close()
connection.close()
