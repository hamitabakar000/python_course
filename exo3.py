mot_de_passe_correct = "python123"
mot_de_passe = ""

while mot_de_passe != mot_de_passe_correct:
    mot_de_passe = input("Entrez le mot de passe : ")
    
    if mot_de_passe != mot_de_passe_correct:
        print("Mot de passe incorrect. Réessayez.")

print("Mot de passe correct ! Accès autorisé.")