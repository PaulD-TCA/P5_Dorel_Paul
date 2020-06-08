DB_NAME = 'purbeurredb'


CATEGORIES = ["Boissons", "Viandes"]#, "Produits laitiers", "Plats préparés"]#,
		#"Produits à tartiner", "Biscuits et gâteaux", "Charcuteries",
		#"Epicerie", "Petit-déjeuners", "Fromages", "Desserts", "Sauces",
		#"Produits de la mer", "Conserves", "Surgelés"]
nutrition_grades = ["A","B"]#,"D","E"]
url_part_1 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0="
url_part_2 = "&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1="
url_part_3 = "&page_size=50&json=true"

#20 ou 50 ou 100 ou 250 ou 500 ou 1000


url_page_open_food_facts = "https://fr.openfoodfacts.org/produit/"

PB_HEADER_DISPLAY = (
				"############################################################\n"
				"#                                                          #\n"
				"#               PUR BEURRE ALIEMENTS SAINS                 #\n"
				"#__________________________________________________________#\n"
				"                                                            \n"
				)


PB_FOOTER_DISPLAY = (
				" __________________________________________________________ \n"
				"#       Faites votre choix à l'aide du pavé numérique,     #\n"
				"#           puis validez avec la touche \"entrée\"           #\n"
				"#                                                          #\n"
				"############################################################\n"
				"\n""\n""\n""\n""\n""\n""\n""\n"
				)

PB_WELCOME_DISPLAY = (

				"                                                            \n"
				"                                                            \n"
				"    Bienvenue dans le programme Pur Beurre Aliments Sains   \n"
				"                                                            \n"
				"                                                            \n"
				"                                                            \n"
				"               Que désirez vous faire?                      \n"
				"                                                            \n"
				"                                                            \n"
				"    1 Rechercher un aliment de substitution                 \n"
				"                                                            \n"
				"    2 Consulter les résultats d'une précédente recherche    \n"
				"                                                            \n"
				"    3 Quitter                                               \n"
				)
