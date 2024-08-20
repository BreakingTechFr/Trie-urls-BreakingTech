import os

# Définition des couleurs
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'

def display_logo():
    logo = """
  _______          _            _    _          _           ____                          _      _                   _______                 _     
 |__   __|        (_)          | |  | |        | |         |  _ \                        | |    (_)                 |__   __|               | |    
    | |     _ __   _    ___    | |  | |  _ __  | |  ___    | |_) |  _ __    ___    __ _  | | __  _   _ __     __ _     | |      ___    ___  | |__  
    | |    | '__| | |  / _ \   | |  | | | '__| | | / __|   |  _ <  | '__|  / _ \  / _` | | |/ / | | | '_ \   / _` |    | |     / _ \  / __| | '_ \ 
    | |    | |    | | |  __/   | |__| | | |    | | \__ \   | |_) | | |    |  __/ | (_| | |   <  | | | | | | | (_| |    | |    |  __/ | (__  | | | |
    |_|    |_|    |_|  \___|    \____/  |_|    |_| |___/   |____/  |_|     \___|  \__,_| |_|\_\ |_| |_| |_|  \__, |    |_|     \___|  \___| |_| |_|
                                                                                                              __/ |                                
                                                                                                             |___/                                           
    """
    print(Colors.BLUE + logo + Colors.RESET)

def nettoyer_terminal():
    # Effacer le terminal en fonction du système d'exploitation
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour macOS et Linux
        os.system('clear')

def nettoyer_url(url):
    # Suppression des préfixes spécifiques
    if url.startswith("www."):
        url = url[4:]
    elif url.startswith("http://www."):
        url = url[11:]
    elif url.startswith("https://www."):
        url = url[12:]
    elif url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    
    # Suppression du caractère '/' à la fin de l'URL
    if url.endswith("/"):
        url = url[:-1]
    
    return url

def analyser_et_nettoyer_fichier(fichier):
    fichier = fichier.strip('\'"')

    if not os.path.exists(fichier):
        print(f"Le fichier '{fichier}' n'existe pas ou le chemin est incorrect.")
        return []
    
    try:
        with open(fichier, 'r') as f:
            urls = f.readlines()
        urls_nettoyees = [nettoyer_url(url.strip()) for url in urls]
        return urls_nettoyees
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier '{fichier}': {e}")
        return []

def comparer_fichiers(fichier1, fichier2):
    fichier1 = fichier1.strip('\'"')
    fichier2 = fichier2.strip('\'"')

    # Nettoyer les URLs avant comparaison
    urls1 = set(analyser_et_nettoyer_fichier(fichier1))
    urls2 = set(analyser_et_nettoyer_fichier(fichier2))
    
    if not urls1 or not urls2:
        print("La comparaison a échoué car l'un des fichiers est vide ou inaccessible.")
        return
    
    # URLs qui sont dans le premier fichier mais pas dans le second
    urls_finales = urls1 - urls2

    output_fichier = "trie-des-deux-fichiers.txt"
    try:
        with open(output_fichier, 'w') as f_out:
            for url in urls_finales:
                f_out.write(url + "\n")
        print(f"Les URLs finales ont été sauvegardées dans '{output_fichier}'")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'écriture dans le fichier '{output_fichier}': {e}")

def menu():
    nettoyer_terminal()  # Effacer le terminal avant d'afficher le menu
    display_logo()       # Afficher le logo

    while True:
        print(Colors.GREEN + "\nMenu:" + Colors.RESET)
        print(Colors.YELLOW + "1. Comparer deux fichiers .txt et trouver les URLs uniques au premier fichier" + Colors.RESET)
        print(Colors.RED + "2. Quitter" + Colors.RESET)

        choix = input(Colors.ORANGE + "Veuillez entrer votre choix: " + Colors.RESET)

        if choix == "1":
            fichier1 = input(Colors.BLUE + "Veuillez glisser déposer ici, le fichier .txt des nouvelles urls: " + Colors.RESET)
            fichier2 = input(Colors.BLUE + "Veuillez glisser déposer ici, le fichier .txt des urls déjà existantes: " + Colors.RESET)
            comparer_fichiers(fichier1, fichier2)

        elif choix == "2":
            print(Colors.RED + "Au revoir!" + Colors.RESET)
            break

        else:
            print(Colors.RED + "Choix invalide. Veuillez réessayer." + Colors.RESET)

if __name__ == "__main__":
    menu()
