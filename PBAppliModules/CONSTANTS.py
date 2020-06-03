pbhost = "localhost"
pbuser = "non-root"
pbpassword = "123"
pbdatabase = "purbeurredb"

categories = ["Boissons", "Viandes"]#, "Produits laitiers", "Plats préparés",
		#"Produits à tartiner", "Biscuits et gâteaux", "Charcuteries",
		#"Epicerie", "Petit-déjeuners", "Fromages", "Desserts", "Sauces",
		#"Produits de la mer", "Conserves", "Surgelés"]
nutrition_grades = ["A","B","D","E"]
urlp1 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0="
urlp2 = "&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1="
urlp3 = "&page_size=50&json=true"

#20 ou 50 ou 100 ou 250 ou 500 ou 1000


urlpageoff = "https://fr.openfoodfacts.org/produit/"
