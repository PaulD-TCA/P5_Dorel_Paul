#! /usr/bin/env python3
# coding: utf-8

import json
import requests
import mysql.connector

class database_fill:

	def __init__(self,constants):
		self.host = constants.pbhost
		self.user = constants.pbuser
		self.password = constants.pbpassword
		self.database = constants.pbdatabase
		self.categories = constants.categories
		self.nutrition_grades = constants.nutrition_grades
		self.urlp1 = constants.urlp1
		self.urlp2 = constants.urlp2
		self.urlp3 = constants.urlp3
		self.urlpageoff = constants.urlpageoff
		self.resp = ""
		self.p_id = 0
		self.p_code = ""
		self.p_name = ""
		self.p_nutrition_grade_fr = ""
		self.p_ingredients_text = ""
		self.p_store = ""
		self.p_categories_hierarchy = ""
		self.p_compared_to_category = ""
		self.p_url = ""
		self.categories_id = ""
		self.c_id = ""
		self.c_name = ""

	def built_data_products(self):# purbeurre data base initialisation
	
		for categorie in self.categories:
			self.c_id = self.categories.index(categorie)
			for nutrition_grade in self.nutrition_grades:
				resp = requests.get(self.urlp1+categorie+
					self.urlp2+nutrition_grade+self.urlp3)
				data = resp.json()
				nb_prods = int(data["count"])# le nombre de produits de la recherche
				page_s = int(data["page_size"])
				prodtowritte = 0
				if page_s <= nb_prods:
					maxproduct = page_s
				else: 
					maxproduct = nb_prods
				while prodtowritte < maxproduct:
					try:			
						database_login = mysql.connector.connect(user = self.user, 
							password = self.password, host = self.host, database = self.database)
						cursor = database_login.cursor()						
						self.p_id = self.p_id + 1
						self.p_code = data["products"][prodtowritte]["code"]
						self.p_name = data["products"][prodtowritte]["product_name"]
						self.p_nutrition_grade_fr = data["products"][prodtowritte]["nutrition_grade_fr"]
						self.p_ingredients_text = data["products"][prodtowritte]["ingredients_text"]
						self.p_store = data["products"][prodtowritte]["stores"]
						self.p_compared_to_category = data["products"][prodtowritte]["compared_to_category"]
						self.p_url = self.urlpageoff + self.p_code
						self.categories_id = self.c_id + 1
						prodtowritte = prodtowritte +1
						cursor.execute("INSERT INTO Products (p_code, p_name, p_nutrition_grade_fr, p_ingredients_text, p_store, p_compared_to_category, p_url, categories_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (self.p_code, self.p_name, self.p_nutrition_grade_fr, self.p_ingredients_text, self.p_store, self.p_compared_to_category, self.p_url, self.categories_id))
						database_login.commit()
						database_login.close()
					except:
						prodtowritte = prodtowritte +1

	def build_data_categories(self):

		for categorie in self.categories:
			database_login = mysql.connector.connect(user = self.user, 
				password = self.password, host = self.host, database = self.database)
			cursor = database_login.cursor()
			c_idtofill = 1
			cursor.execute("INSERT INTO Categories (c_id2, c_name) VALUES (%s, %s)",(c_idtofill, categorie))
			c_idtofill = c_idtofill + 1
			database_login.commit()
			database_login.close()