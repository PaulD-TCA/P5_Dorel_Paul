#! /usr/bin/env python3
# coding: utf-8

import requests
import mysql.connector

class database_ini:
	def __init__(self,constants):
		self.host = constants.pbhost
		self.user = constants.pbuser
		self.password = constants.pbpassword
		self.database = constants.pbdatabase
		

	def db_ini(self):# purbeurre data base initialisation
		mysql_login = mysql.connector.connect(user = self.user, 
			password = self.password, host = self.host)
		cursor = mysql_login.cursor()
		cursor.execute("DROP DATABASE IF EXISTS purbeurredb")
		cursor.execute("CREATE DATABASE purbeurredb")
		mysql_login.close()

	def table_products(self):# Product table initialisation
		database_login = mysql.connector.connect(user = self.user, 
			password = self.password, host = self.host, database = self.database)
		cursor = database_login.cursor()
		cursor.execute("""CREATE TABLE Products (
			p_id int unsigned NOT NULL AUTO_INCREMENT,
			p_code varchar(50), 
			p_name varchar(200),
			p_nutrition_grade_fr text(1),
			p_ingredients_text varchar(2000),
			p_store varchar(200),
			p_compared_to_category varchar(200),
			p_url varchar(1000),
			categories_id tinyint(3),
			PRIMARY KEY (p_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
		database_login.close()

	def table_categories(self):# Categories table initialisation
		database_login = mysql.connector.connect(user = self.user, 
			password = self.password, host = self.host, database = self.database)
		cursor = database_login.cursor()
		cursor.execute("""CREATE TABLE Categories (
			c_id int unsigned NOT NULL AUTO_INCREMENT,
			c_id2 int,
			c_name varchar(100),
			PRIMARY KEY (c_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
		database_login.close()

	def table_backup(self):# Backup table initialisation
		database_login = mysql.connector.connect(user = self.user, 
			password = self.password, host = self.host, database = self.database)
		cursor = database_login.cursor()
		cursor.execute("""CREATE TABLE Backup (
			b_id int unsigned NOT NULL AUTO_INCREMENT,
			b_date date,
			products_id int,
			PRIMARY KEY (b_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
		database_login.close()

