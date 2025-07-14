def charger_utilisateurs(fichier="utilisateurs.txt"):
    """
    Charge les utilisateurs à partir du fichier.
    Retourne une liste de dictionnaires.
    """
    utilisateurs = []
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                parts = ligne.strip().split(";")
                if len(parts) == 6:
                    utilisateurs.append({
                        "login": parts[0],
                        "nom": parts[1],
                        "prenom": parts[2],
                        "cp": parts[3],
                        "email": parts[4],
                        "mdp": parts[5]
                    })
    except FileNotFoundError:
        pass
    return utilisateurs


def ecrire_utilisateurs(utilisateurs, fichier="utilisateurs.txt"):
    """
    Réécrit la liste complète des utilisateurs dans le fichier.
    """
    try:
        with open(fichier, "w", encoding="utf-8") as f:
            for u in utilisateurs:
                f.write(f"{u['login']};{u['nom']};{u['prenom']};{u['cp']};{u['email']};{u['mdp']}\n")
    except Exception as e:
        print(f"Erreur lors de l'écriture : {e}")


def lire_logins_existants(fichier="utilisateurs.txt"):
    """
    Retourne la liste des logins déjà enregistrés.
    """
    utilisateurs = charger_utilisateurs(fichier)
    return [u["login"] for u in utilisateurs]


def sauvegarder_utilisateur(nom, prenom, cp, email, login, mdp, fichier="utilisateurs.txt"):
    """
    Ajoute un utilisateur à la fin du fichier.
    Le mot de passe est masqué.
    """
    try:
        with open(fichier, "a", encoding="utf-8") as f:
            f.write(f"{login};{nom};{prenom};{cp};{email};{'*' * len(mdp)}\n")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")


def supprimer_utilisateur(login, fichier="utilisateurs.txt"):
    """
    Supprime un utilisateur par son login (s’il existe).
    """
    utilisateurs = charger_utilisateurs(fichier)
    utilisateurs = [u for u in utilisateurs if u["login"] != login]
    ecrire_utilisateurs(utilisateurs, fichier)
    print(f"✅ Utilisateur '{login}' supprimé avec succès (s’il existait).")


def mettre_a_jour_utilisateur(login, nouveau_email=None, nouveau_mdp=None, fichier="utilisateurs.txt"):
    """
    Met à jour l'email et/ou le mot de passe d'un utilisateur identifié par son login.
    """
    utilisateurs = charger_utilisateurs(fichier)
    modifié = False
    for u in utilisateurs:
        if u["login"] == login:
            if nouveau_email:
                u["email"] = nouveau_email
            if nouveau_mdp:
                u["mdp"] = "*" * len(nouveau_mdp)
            modifié = True
            break
    if modifié:
        ecrire_utilisateurs(utilisateurs, fichier)
        print(f"✅ Utilisateur '{login}' mis à jour avec succès.")
    else:
        print(f"❌ Aucun utilisateur trouvé avec le login '{login}'.")


def afficher_utilisateurs(fichier="utilisateurs.txt"):
    """
    Affiche tous les utilisateurs du fichier en masquant leur mot de passe.
    """
    utilisateurs = charger_utilisateurs(fichier)
    if not utilisateurs:
        print("📭 Aucun utilisateur enregistré.")
        return

    print("\n=== Liste des utilisateurs ===")
    for i, u in enumerate(utilisateurs, 1):
        print(f"\nUtilisateur {i} :")
        print(f"  Nom      : {u['nom']}")
        print(f"  Prénom   : {u['prenom']}")
        print(f"  CP       : {u['cp']}")
        print(f"  Email    : {u['email']}")
        print(f"  Login    : {u['login']}")
        print(f"  Mot de passe : {u['mdp']}")
