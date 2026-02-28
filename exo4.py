try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    
    # Affichage du menu des opérations
    print("\nChoisissez une opération :")
    print("1 : Addition")
    print("2 : Soustraction")
    print("3 : Multiplication")
    print("4 : Division")
    
    choix = input("Votre choix (1-4) : ")
    
    # Traitement selon le choix
    if choix == "1":
        resultat = nombre1 + nombre2
        print(f"Résultat : {nombre1} + {nombre2} = {resultat}")
        
    elif choix == "2":
        resultat = nombre1 - nombre2
        print(f"Résultat : {nombre1} - {nombre2} = {resultat}")
        
    elif choix == "3":
        resultat = nombre1 * nombre2
        print(f"Résultat : {nombre1} * {nombre2} = {resultat}")
        
    elif choix == "4":
        # Vérification de la division par zéro
        if nombre2 == 0:
            print("Erreur : Division par zéro impossible !")
        else:
            resultat = nombre1 / nombre2
            print(f"Résultat : {nombre1} / {nombre2} = {resultat}")
            
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")
        
except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")