#! /usr/bin/env python3
# coding: utf-8

import requests
import mysql.connector

class database_ini:
	def __init__(self):
		self.host = "localhost"
		self.user = "non-root"
		self.password = "123"
		self.database = "purbeurredb"

	def db_ini(self):# purbeurre data base initialisation
		mysql_login = mysql.connector.connect(user = self.user, password = self.password, host = self.host)
		cursor = mysql_login.cursor()
		cursor.execute("CREATE DATABASE purbeurredb")
		mysql_login.close()

	def table_products(self):# Product table initialisation
		database_login = mysql.connector.connect(user = self.user, password = self.password, host = self.host, database = self.database)
		cursor = database_login.cursor()
		cursor.execute("""CREATE TABLE Products (
			p_id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
			p_code varchar(200), 
			p_name varchar(200),
			p_url varchar(200),
			p_nutriscore_grade varchar(5),
			p_store varchar(100),
			p_ingredients_text varchar(200),
			p_categories_tags1 varchar(200),
			PRIMARY KEY (p_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
		database_login.close()

	def table_categories(self):# Categories table initialisation
		database_login = mysql.connector.connect(user = self.user, password = self.password, host = self.host, database = self.database)
		cursor = database_login.cursor()
		cursor.execute("""CREATE TABLE Categories (
			c_id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
			c_name varchar(100),
			c_categories_tags1 varchar(200),
			PRIMARY KEY (c_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
		database_login.close()

	def table_backup(self):# Backup table initialisation
		database_login = mysql.connector.connect(user = self.user, password = self.password, host = self.host, database = self.database)
		cursor = database_login.cursor()
		cursor.execute("""CREATE TABLE Backup (
			b_id smallint(5) unsigned NOT NULL AUTO_INCREMENT,
			p_id smallint(5),
			b_date date,
			PRIMARY KEY (b_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8;""")
		database_login.close()


