# P5_Dorel_Paul
Utilisez les données publiques de l'OpenFoodFacts

# Enoncé
La startup Pur Beurre possède le restaurant Ratatouille. Ses clients souhaitent changer leurs habitudes alimentaire. Pour les aider, la société Pur Beurre à besoin d'un programme qui proposera à ses utilisateurs des substituts sain aux aliments qu'ils auront sélectionnés.

# Notice d'utilisation du programme
L'utilisateur fait ses choix dans en entrant les numéros associés aux menus
- L'utilisateur démarre le programme
- Le terminal affiche 3 choix.
	- 1 Quels aliments souhaitez-vous remplacer?
	=> L'utilisateur choisit dans une liste de catégories puis des aliments
	- 2 Retrouver mes aliments substitués
	=> L'utilisateur peut afficher le résultat de recherches précédentes
	- 3 Quitter 

# Avant d'utiliser le programme:
	- 1 ==> installer Python3, MySQL et les librairies indiquées
	- 2 ==> dans le dossier "PBAppliModules" ouvrir le fichier "user_data.py" et y remplacer "your_host", "your_user" et your_password" par vos identifiants MySQL.
	- 3 ==> Lancer le script "P5_02_script.py" dans votre terminal. Compter entre 9 et 10 minutes pour la création de la base de données
	- 4 ==> Vous pouver le programme en lançant le fichier "P5_03_Code_Source_Main.py" dans votre terminal.

# Librairies
- json
- requests
- mysql-connector