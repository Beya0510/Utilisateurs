import re

# On crée une expression régulière qui accepte :
# - les lettres accentuées majuscules et minuscules
# - les espaces
# - les traits d’union
# En Unicode, \w ne suffit pas : on liste les lettres accentuées ou on utilise un groupe unicode

def check_nom_prenom(nom, prenom):
    """
    Vérifie que nom et prénom ne sont pas identiques,
    et ne contiennent que des lettres (même accentuées), des espaces ou des tirets.
    """
    if nom.lower() == prenom.lower():
        return False, "Le nom et le prénom ne peuvent pas être identiques."

    # Regex pour lettres accentuées, espaces et tirets (compatible UTF-8)
    regex_nom = r"^[A-Za-zÀ-ÖØ-öø-ÿœŒçÇ\- ]+$"

    if not re.fullmatch(regex_nom, nom):
        return False, "Le nom ne peut contenir que des lettres (accentuées ou non), des espaces et des traits d’union."

    if not re.fullmatch(regex_nom, prenom):
        return False, "Le prénom ne peut contenir que des lettres (accentuées ou non), des espaces et des traits d’union."

    return True, ""


def check_cp(cp):
    """
    Vérifie que le code postal est un entier entre 1000 et 9999 (valide en Belgique).
    """
    if cp.isdigit() and 1000 <= int(cp) <= 9999:
        return True, ""
    return False, "Le code postal doit être un entier belge valide (entre 1000 et 9999)."


def check_email(email):
    """
    Vérifie le format d'email (autorise lettres, chiffres, points et tirets).
    N’autorise pas les caractères spéciaux autres que . ou -
    """
    if re.fullmatch(r"[A-Za-z0-9\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z]{2,}", email):
        return True, ""
    return False, "L'email est invalide. Utilisez uniquement des lettres, chiffres, points ou tirets."


def check_login(login):
    """
    Vérifie que le login est uniquement en lettres minuscules sans caractères spéciaux.
    """
    if re.fullmatch(r"[a-z]+", login):
        return True, ""
    return False, "Le login doit être uniquement en minuscules, sans caractères spéciaux."


def check_mdp(mdp):
    """
    Vérifie que le mot de passe contient :
    - au moins 10 caractères
    - au moins une majuscule
    - au moins une minuscule
    - au moins un chiffre
    - au moins un caractère spécial
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
