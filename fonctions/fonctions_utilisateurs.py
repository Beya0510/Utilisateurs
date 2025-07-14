import re


def check_nom_prenom(nom, prenom):
    """
    Vérifie que nom et prénom ne sont pas égaux et ne contiennent que des lettres ou des traits d'union.
    """
    if nom.lower() == prenom.lower():
        return False, "Le nom et le prénom ne peuvent pas être identiques."

    if not re.fullmatch(r"[A-Za-z\- ]+", nom):
        return False, "Le nom ne peut contenir que des lettres et des traits d’union."

    if not re.fullmatch(r"[A-Za-z\- ]+", prenom):
        return False, "Le prénom ne peut contenir que des lettres et des traits d’union."

    return True, ""


def check_cp(cp):
    """
    Vérifie que le code postal est un entier à 4 chiffres entre 1000 et 9999 (valide en Belgique).
    """
    if cp.isdigit() and 1000 <= int(cp) <= 9999:
        return True, ""
    return False, "Le code postal doit être un entier belge valide (entre 1000 et 9999)."


def check_email(email):
    """
    Vérifie la validité d'un email (format et caractères autorisés).
    """
    if re.fullmatch(r"[A-Za-z0-9\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z]{2,}", email):
        return True, ""
    return False, "L'email est invalide. Utilisez uniquement des lettres, chiffres, points ou tirets."


def check_login(login):
    """
    Vérifie que le login ne contient que des lettres minuscules sans caractère spécial.
    """
    if re.fullmatch(r"[a-z]+", login):
        return True, ""
    return False, "Le login doit être uniquement en minuscules, sans caractères spéciaux."


def check_mdp(mdp):
    """
    Vérifie que le mot de passe fait au moins 10 caractères, avec 1 majuscule, 1 minuscule,
    1 chiffre et 1 caractère spécial.
    """
    if len(mdp) < 10:
        return False, "Le mot de passe doit contenir au moins 10 caractères."

    if not re.search(r"[A-Z]", mdp):
        return False, "Le mot de passe doit contenir au moins une majuscule."

    if not re.search(r"[a-z]", mdp):
        return False, "Le mot de passe doit contenir au moins une minuscule."

    if not re.search(r"\d", mdp):
        return False, "Le mot de passe doit contenir au moins un chiffre."

    if not re.search(r"[^\w\s]", mdp):  # caractère spécial
        return False, "Le mot de passe doit contenir au moins un caractère spécial."

    return True, ""
