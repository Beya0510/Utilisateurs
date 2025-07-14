# Importation des fonctions de validation
from fonctions.fonctions_utilisateurs import (
    check_nom_prenom,
    check_cp,
    check_email,
    check_login,
    check_mdp
)

# Importation des fonctions de gestion des utilisateurs
from fonctions.crud_utilisateurs import (
    lire_logins_existants,
    sauvegarder_utilisateur,
    supprimer_utilisateur,
    mettre_a_jour_utilisateur,
    afficher_utilisateurs
)



def encoder_utilisateur(logins_existants):
    """
    Permet d'encoder un utilisateur en validant chaque champ.
    Si le login est déjà utilisé, on redemande une saisie.
    Une fois l'utilisateur valide, on le sauvegarde.
    """
    print("\n=== Nouvel utilisateur ===")
    while True:
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        ok, msg = check_nom_prenom(nom, prenom)
        if not ok:
            print("Erreur :", msg)
            continue

        cp = input("Code postal : ")
        ok, msg = check_cp(cp)
        if not ok:
            print("Erreur :", msg)
            continue

        email = input("Email : ")
        ok, msg = check_email(email)
        if not ok:
            print("Erreur :", msg)
            continue

        login = input("Login : ")
        if login in logins_existants:
            print("Erreur : login déjà utilisé. Veuillez en choisir un autre.")
            continue
        ok, msg = check_login(login)
        if not ok:
            print("Erreur :", msg)
            continue

        mdp = input("Mot de passe : ")
        ok, msg = check_mdp(mdp)
        if not ok:
            print("Erreur :", msg)
            continue

        print("\n✅ Utilisateur encodé avec succès.")
        print("Nom :", nom)
        print("Prénom :", prenom)
        print("Code postal :", cp)
        print("Email :", email)
        print("Login :", login)
        print("Mot de passe :", '*' * len(mdp))

        logins_existants.append(login)
        sauvegarder_utilisateur(nom, prenom, cp, email, login, mdp)
        break


def main():
    print("=== Gestion des utilisateurs ===")
    logins_existants = lire_logins_existants()

    while True:
        print("\nOptions disponibles :")
        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Mettre à jour un utilisateur")
        print("4. Quitter")
        print("5. Afficher tous les utilisateurs")  # ✅ Ajout du choix

        choix = input("Votre choix : ")

        if choix == "1":
            encoder_utilisateur(logins_existants)

        elif choix == "2":
            login = input("Entrez le login à supprimer : ")
            supprimer_utilisateur(login)
            if login in logins_existants:
                logins_existants.remove(login)

        elif choix == "3":
            login = input("Login de l'utilisateur à mettre à jour : ")
            changer_email = input("Changer email ? (laisser vide pour ne pas modifier) : ")
            changer_mdp = input("Changer mot de passe ? (laisser vide pour ne pas modifier) : ")

            if changer_email:
                ok, msg = check_email(changer_email)
                if not ok:
                    print("Erreur :", msg)
                    continue

            if changer_mdp:
                ok, msg = check_mdp(changer_mdp)
                if not ok:
                    print("Erreur :", msg)
                    continue

            mettre_a_jour_utilisateur(login, changer_email or None, changer_mdp or None)

        elif choix == "4":
            print("Fin de l'application.")
            break

        elif choix == "5":
            afficher_utilisateurs()

        else:
            print("Option invalide.")


if __name__ == "__main__":
    main()
