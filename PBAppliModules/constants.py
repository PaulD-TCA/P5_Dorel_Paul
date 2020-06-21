#! /usr/bin/env python3
# coding: utf-8

CATEGORIES = ["Boissons", "Viandes", "Produits laitiers", "Plats préparés",
		"Produits à tartiner", "Biscuits et gâteaux", "Charcuteries",
		"Epicerie", "Petit-déjeuners", "Fromages", "Desserts", "Sauces",
		"Produits de la mer", "Conserves", "Surgelés"]
NUTRITION_GRADES = ["A","B","D","E"]
URL_PART_1 = "https://fr.openfoodfacts.org/cgi/search.pl?action="\
            "process&tagtype_0=categories&tag_contains_0=contains&tag_0="
URL_PART_2 = "&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1="
URL_PART_3 = "&page_size=500&json=true"
#20 or 50 or 100 or 250 or 500 or 1000


URL_OPEN_FOOD_FACTS = "https://fr.openfoodfacts.org/produit/"

PB_HEADER_DISPLAY = (
				"\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n"
				"\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n"
				"\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n""\n"

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

PB_SUBSTITUTION_DISPLAY = (
				"                                                            \n"
				"                  ________________________                  \n"
				"                                                            \n"
				"               Que désirez vous faire?                      \n"
				"                                                            \n"
				"                                                            \n"
				"    1 Sauvegarder votre recherche                           \n"
				"                                                            \n"
				"    2 Effectuer une nouvelle recherche                      \n"
				"                                                            \n"
				"    3 Quitter                                               \n"
				)

PB_CATEGORIES_DISPLAY = (

				"                  Catégories proposées:                     \n"
				)

PB_PROPOSITION_JF_DISPLAY = (

				"           Proposition d'aliments à substituer:             \n"
				)

PB_PROPOSITION_HF_DISPLAY = (

				"           Proposition d'aliments à substituer:             \n"
				)
