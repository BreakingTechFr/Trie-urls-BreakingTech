# Trie-urls-BreakingTech

![Capture d’écran 2024-08-20 à 16 08 01](https://github.com/user-attachments/assets/a32d7bed-84c4-4adf-9aca-51fed7aed841)

Cette application Python est un outil de comparaison d'URLs qui permet de traiter efficacement deux fichiers .txt contenant des listes d'URLs. Elle est particulièrement utile pour identifier les nouvelles URLs qui ne sont pas présentes dans un fichier existant.

# Installation :
- Installez les dépendances avec la commande :
```shell![Capture d’écran 2024-08-19 à 09 19 09](https://github.com/user-attachments/assets/3a408e51-26b6-4ec0-9738-cd11918b4f17)
pip install requirements.txt
```
- Lancez le fichier trie.py en utilisant la commande :
```shell
python trie.py
```

# Fonctionnalités :
Nettoyage automatique des URLs : Avant la comparaison, l'application nettoie automatiquement chaque URL des fichiers en supprimant les préfixes www., http://, https://, https://www., ou http://www.. De plus, si une URL se termine par un caractère /, celui-ci est également supprimé pour assurer une comparaison correcte.

Comparaison d'URLs : L'application compare les deux fichiers .txt après nettoyage des URLs et extrait les URLs qui sont présentes uniquement dans le premier fichier (c'est-à-dire les nouvelles URLs qui ne sont pas déjà dans le second fichier).

Génération d'un fichier de résultats : Les résultats de la comparaison sont automatiquement sauvegardés dans un fichier nommé trie-des-deux-fichiers.txt, qui contient toutes les URLs uniques du premier fichier.

# Utilisation :
Glisser-déposer des fichiers : L'utilisateur est invité à glisser-déposer les fichiers .txt contenant les listes d'URLs dans le terminal. Le premier fichier doit contenir les nouvelles URLs à analyser, et le second fichier doit contenir les URLs déjà existantes.

Nettoyage et comparaison : Le programme nettoie les URLs des deux fichiers avant de procéder à la comparaison pour s'assurer que les URLs sont dans un format cohérent.

Résultat : Les URLs qui sont présentes dans le premier fichier mais absentes du second sont sauvegardées dans un fichier trie-des-deux-fichiers.txt, créé automatiquement dans le répertoire courant.

# Exemple d'utilisation :
Supposons que vous ayez deux fichiers :

nouvelles_urls.txt : Contient une liste d'URLs à vérifier.
urls_existantes.txt : Contient une liste d'URLs déjà existantes.
En utilisant l'application, vous pourrez identifier rapidement toutes les nouvelles URLs présentes dans nouvelles_urls.txt qui ne sont pas dans urls_existantes.txt.


## Suivez-nous

- [@breakingtechfr](https://twitter.com/BreakingTechFR) sur Twitter.
- [Facebook](https://www.facebook.com/BreakingTechFr/) likez notre page.
- [Instagram](https://www.instagram.com/breakingtechfr/) taguez nous sur vos publications !
- [Discord](https://discord.gg/VYNVBhk) pour parler avec nous !
