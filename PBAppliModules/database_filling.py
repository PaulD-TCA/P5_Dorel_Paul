#! /usr/bin/env python3
# coding: utf-8

import json
import requests
import mysql.connector

class database_fill:
	def __init__(self):
		self.host = ""
		self.user = ""
		self.password = ""
		self.database = "purbeurredb"




		self.categories = ["Boissons", "Viandes", "Produits laitiers", 
		"Plats préparés", "Produits à tartiner", "Biscuits et gâteaux", 
		"Charcuteries", "Epicerie", "Petit-déjeuners", "Fromages", "Desserts", 
		"Sauces", "Produits de la mer", "Conserves", "Surgelés"]



	def read_openfoodfacts(self):# purbeurre data base initialisation


#	def writte_purbeurre_db(self):
