# Discord Bot

Ce bot Discord qui encule des serveurs peut faire.

## Fonctionnalités

- **Commande `pub`** : Envoie un message de promotion aux administrateurs et kick tous les membres du serveur, puis crée un salon de spam.
- **Commande `randomban`** : Ban un utilisateur aléatoire du serveur.
- **Commande `randomkick`** : Kick un utilisateur aléatoire du serveur.
- **Renommer le serveur** : Permet de renommer le serveur à l'aide d'une commande spécifique. 
- **Commande `exit`** : Quitte le serveur dans lequel le bot est présent.

## Installation

### Prérequis

- Python 3.11 ou supérieur doit être installé.

### Installation automatique

Pour installer automatiquement Python et les dépendances nécessaires, exécutez le fichier `setup.bat`. Ce script :

1. Vérifie si Python est installé, et si ce n'est pas le cas, le télécharge et l'installe.
2. Installe les dépendances nécessaires :
   - `colorama`
   - `discord.py`

### Utilisation

Après l'installation, lancez le bot avec la commande suivante :

```bash
python main.py
