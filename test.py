#1.Imprimer du texte :

print("bonjour, monde !")

# 2. Variables :

# Variables de type entier, flottant et chaine de caracteres 
x = 10
y = 3.14
nom = "Alice"
print(x, y, nom)

# 3. opereation mathematique

a = 5
b = 2
somme = a + b
produit = a * b
quotient = a / b
reste = a % b
puissance = a ** b
print(somme, produit, quotient, reste, puissance)

# 4. conditions (if/else)

age = 18
if age >= 18: 
    print("tu es majeur.")
else:
    print("Tu es mineur.")

#. boucles ( for et while)

# Boucle for:


for i in range (5):
    print("i vaut :", i)

# Boucle while :


compteur = 0
while compteur <5:
    print("compteur :", compteur)
    compteur += 1

# 6. Foctions :

def salut(nom):
    return f"Salut, {nom}!"

message = salut("Alice")
print(message)

# 7. listes :

fruits = ["pomme,", "banane", "orange" ]
print(fruits)
fruits.append("mangue") # Ajouter un element 
print(fruits[1])  # Acceder a un element 

# 8. Dictionneres 

personne = {"nom": "Alice", "age": 25, "Ville": "Paris"}
print(personne["nom"])
personne["profession"] = "Ingenieure"
print(personne)

# 9. Boucle sur une liste ou un dictionnaire :

# Liste


for fruit in fruits:
    print(fruit)

# Dictionnaire : 


for cle, valeur in personne.items():
    print(cle, ":", valeur)

# 10. Gestion des erreurs (try/except) :

try :
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zero !:")
# 11. Entree utilisateur :


nom = input("Quel est ton nom ? ")
print("Bonjour,", nom)

# 12. Lire et ecrire dans un fichier : 

# Ecrire dans un fichier : 


with open("mon_fichier.txt", "w") as fichier:
    fichier.write("Ceci est un texte ecrit dans un fichier.")

    # Lire un fichier :


    with open("mon_fichier.txt", "r") as fichier:
        contenu = fichier.read()
        print(contenu)

# 13. Classes et objets (Poo - Programation Orientee Objet) :

class Personne:
    def _init_(self, nom, age):
        self.nom = nom 
        self.age = age 

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")

personne1 = Personne("Alice", 25)
personne1.se_presenter()