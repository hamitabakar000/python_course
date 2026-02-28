contacts = []

# Boucle principale du menu
while True:
    print("\n--- MENU CARNET D'ADRESSES ---")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Quitter")
    
    choix = input("Votre choix (1-3) : ")
    
    if choix == "1":
        # Ajout d'un contact
        nom = input("Entrez le nom du contact : ")
        contacts.append(nom)
        print(f"Contact '{nom}' ajouté avec succès!")
        
    elif choix == "2":
        # Affichage des contacts avec numérotation
        if contacts:
            print("\nListe des contacts :")
            for index, contact in enumerate(contacts):
                print(f"{index + 1}. {contact}")
        else:
            print("Aucun contact dans la liste.")
            
    elif choix == "3":
        # Quitter le programme
        print("Au revoir!")
        break
        
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")