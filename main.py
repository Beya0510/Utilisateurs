from fonctions.fonctions_utilisateurs import (
    check_nom_prenom,
    check_cp,
    check_email,
    check_login,
    check_mdp
)


def encoder_utilisateur(utilisateur_numero):
    print(f"\n=== Encodage de l'utilisateur {utilisateur_numero} ===")

    while True:
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        valid, msg = check_nom_prenom(nom, prenom)
        if not valid:
            print("Erreur :", msg)
            continue

        cp = input("Code postal : ")
        valid, msg = check_cp(cp)
        if not valid:
            print("Erreur :", msg)
            continue

        email = input("Email : ")
        valid, msg = check_email(email)
        if not valid:
            print("Erreur :", msg)
            continue

        login = input("Login (tout en minuscules) : ")
        valid, msg = check_login(login)
        if not valid:
            print("Erreur :", msg)
            continue

        mdp = input("Mot de passe : ")
        valid, msg = check_mdp(mdp)
        if not valid:
            print("Erreur :", msg)
            continue

        print("\n✅ Données valides !")
        print("Nom :", nom)
        print("Prénom :", prenom)
        print("Code postal :", cp)
        print("Email :", email)
        print("Login :", login)
        print("Mot de passe :", '*' * len(mdp))
        return login  # pour vérifier la redondance


def main():
    print("Bienvenue dans l'encodage des utilisateurs")

    login1 = encoder_utilisateur(1)
    print("\nVeuillez entrer un second utilisateur.")

    while True:
        login2 = encoder_utilisateur(2)
        if login2 == login1:
            print("Erreur : le login est déjà utilisé. Veuillez en choisir un autre.")
        else:
            break

    print("\n🎉 Les deux utilisateurs ont été encodés avec succès !")


if __name__ == "__main__":
    main()
