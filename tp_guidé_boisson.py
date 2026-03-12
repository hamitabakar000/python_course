# =============================================================================
# SYSTÈME DE BOISSONS - POO Python
# TP MI-GUIDÉ | Licence Développement Web Avancé | 2025/2026
# =============================================================================

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# =============================================================================
# PARTIE 1 : Classe abstraite de base
# =============================================================================

class Boisson(ABC):
    """
    Classe abstraite représentant une boisson générique.
    Toute boisson concrète DOIT implémenter cout() et description().
    """

    @abstractmethod
    def cout(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    def __add__(self, other: 'Boisson') -> 'BoissonCombinee':
        """Permet de combiner deux boissons avec l'opérateur +"""
        return BoissonCombinee(self, other)

    def afficher_commande(self):
        """Affiche un résumé formaté de la boisson"""
        print(f"Commande : {self.description()}")
        print(f"Prix : {self.cout():.1f}€")


# =============================================================================
# PARTIE 2 : Boissons concrètes
# =============================================================================

class Cafe(Boisson):
    """Un café simple à 2.0€"""

    def cout(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Café simple"


class The(Boisson):
    """Un thé à 1.5€"""

    def cout(self) -> float:
        return 1.5

    def description(self) -> str:
        return "Thé"


class ChocolatChaud(Boisson):
    """Un chocolat chaud à 2.5€"""

    def cout(self) -> float:
        return 2.5

    def description(self) -> str:
        return "Chocolat chaud"


# =============================================================================
# PARTIE 3 : Décorateurs d'ingrédients (Patron de conception Decorator)
# =============================================================================

class DecorateurBoisson(Boisson):
    """
    Classe décorateur de base.
    Enveloppe une boisson existante pour y ajouter des ingrédients.
    """

    def __init__(self, boisson: Boisson):
        self._boisson = boisson


class Lait(DecorateurBoisson):
    """Ajoute du lait (+0.5€)"""

    def cout(self) -> float:
        return self._boisson.cout() + 0.5

    def description(self) -> str:
        return self._boisson.description() + ", Lait"


class Sucre(DecorateurBoisson):
    """Ajoute du sucre (+0.2€)"""

    def cout(self) -> float:
        return self._boisson.cout() + 0.2

    def description(self) -> str:
        return self._boisson.description() + ", Sucre"


class Caramel(DecorateurBoisson):
    """Ajoute du caramel (+0.7€)"""

    def cout(self) -> float:
        return self._boisson.cout() + 0.7

    def description(self) -> str:
        return self._boisson.description() + ", Caramel"


# =============================================================================
# PARTIE 4 : Combinaison de boissons
# =============================================================================

class BoissonCombinee(Boisson):
    """
    Représente la combinaison de deux boissons.
    Créée automatiquement via l'opérateur + grâce à __add__.
    """

    def __init__(self, boisson1: Boisson, boisson2: Boisson):
        self._boisson1 = boisson1
        self._boisson2 = boisson2

    def cout(self) -> float:
        return self._boisson1.cout() + self._boisson2.cout()

    def description(self) -> str:
        return self._boisson1.description() + " + " + self._boisson2.description()


# =============================================================================
# PARTIE 5 : Représentation d'un client (dataclass)
# =============================================================================

@dataclass
class Client:
    """
    Représente un client du café.
    Utilise @dataclass qui génère automatiquement __init__, __repr__, __eq__.
    """
    nom: str
    numero: int
    points_fidelite: int = 0


# =============================================================================
# PARTIE 7.1 : Classe Commande
# =============================================================================

class Commande:
    """
    Représente une commande passée par un client.
    Contient un client et une liste de boissons.
    """

    def __init__(self, client: Client):
        self.client = client
        self.boissons: list[Boisson] = []

    def ajouter_boisson(self, boisson: Boisson):
        """Ajoute une boisson à la commande"""
        self.boissons.append(boisson)

    def prix_total(self) -> float:
        """Calcule le prix total de toutes les boissons"""
        return sum(b.cout() for b in self.boissons)

    def afficher(self):
        """Affiche le contenu complet de la commande"""
        print(f"=== Commande de {self.client.nom} (N°{self.client.numero}) ===")
        for boisson in self.boissons:
            print(f"  - {boisson.description()} : {boisson.cout():.2f}€")
        print(f"  TOTAL : {self.prix_total():.2f}€")


# =============================================================================
# PARTIE 7.2 : Types de commandes (héritage)
# =============================================================================

class CommandeSurPlace(Commande):
    """Commande consommée sur place"""

    def afficher(self):
        print("[ COMMANDE SUR PLACE ]")
        super().afficher()
        print("  → Service en salle\n")


class CommandeEmporter(Commande):
    """Commande à emporter"""

    def afficher(self):
        print("[ COMMANDE À EMPORTER ]")
        super().afficher()
        print("  → Emballage fourni\n")


# =============================================================================
# PARTIE 7.3 : Programme de fidélité
# =============================================================================

class Fidelite:
    """
    Gère le système de fidélité.
    1 point par euro dépensé (arrondi à l'entier inférieur).
    """

    def ajouter_points(self, client: Client, montant: float):
        """Ajoute des points de fidélité selon le montant de la commande"""
        points_gagnes = int(montant)
        client.points_fidelite += points_gagnes
        print(f"   +{points_gagnes} points fidélité → Total : {client.points_fidelite} points")


# =============================================================================
# PARTIE 7.4 : Héritage multiple - CommandeFidele
# =============================================================================

class CommandeFidele(Commande, Fidelite):
    """
    Commande intégrant le programme de fidélité.
    Hérite de Commande (gestion des boissons) ET de Fidelite (points).
    """

    def valider(self):
        """Valide la commande et attribue les points au client"""
        total = self.prix_total()
        print(f"\n Validation de la commande...")
        self.afficher()
        self.ajouter_points(self.client, total)


# =============================================================================
# PARTIE 7.5 : TEST COMPLET DU SYSTÈME
# =============================================================================

if __name__ == "__main__":

    print("=" * 60)
    print("  SYSTÈME DE BOISSONS - DÉMONSTRATION COMPLÈTE")
    print("=" * 60)

    # --- Partie 2 : Boissons simples ---
    print("\n PARTIE 2 — Boissons de base :")
    cafe = Cafe()
    the = The()
    cafe.afficher_commande()
    print()
    the.afficher_commande()

    # --- Partie 3 : Ingrédients (décorateurs) ---
    print("\n PARTIE 3 — Ajout d'ingrédients :")
    cafe_lait_sucre = Sucre(Lait(Cafe()))
    cafe_lait_sucre.afficher_commande()
    print()
    the_caramel = Caramel(The())
    the_caramel.afficher_commande()

    # --- Partie 4 : Combinaison de boissons ---
    print("\n PARTIE 4 — Combinaison de boissons :")
    menu = Cafe() + The()
    menu.afficher_commande()

    # --- Partie 5 : Client ---
    print("\n PARTIE 5 — Création d'un client :")
    client = Client(nom="Alice", numero=42, points_fidelite=0)
    print(f"  Client : {client}")

    # --- Partie 7 : Commandes ---
    print("\n PARTIE 7 — Commande sur place :")
    commande1 = CommandeSurPlace(client)
    commande1.ajouter_boisson(Sucre(Lait(Cafe())))
    commande1.ajouter_boisson(The())
    commande1.afficher()

    print("\n PARTIE 7 — Commande à emporter :")
    commande2 = CommandeEmporter(client)
    commande2.ajouter_boisson(Caramel(Cafe()))
    commande2.ajouter_boisson(ChocolatChaud())
    commande2.afficher()

    print("\n PARTIE 7 — Commande avec fidélité :")
    commande_fidele = CommandeFidele(client)
    commande_fidele.ajouter_boisson(Sucre(Lait(Cafe())))
    commande_fidele.ajouter_boisson(Caramel(The()))
    commande_fidele.valider()

    print(f"\n Points finaux de {client.nom} : {client.points_fidelite} points")
    print("\n" + "=" * 60)