age = int(input("Entrez votre âge : "))

# Détermination de la catégorie
if age <= 12:
    categorie = "Enfant"
elif age <= 17:
    categorie = "Adolescent"
elif age <= 64:
    categorie = "Adulte"
else:
    categorie = "Senior"

# Affichage du résultat
print(f"Vous êtes un(e) {categorie}.")