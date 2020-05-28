#! /usr/bin/env python3
# coding: utf-8


import json
import requests
import mysql.connector

#modules import
from PBAppliModules import database_initialization, database_filling, constants

if __name__ == '__main__':
	#Instances creation
	database = database_initialization.database_ini(constants)#
	filling = database_filling.database_fill(constants)

	#Data base initialisation
	database.db_ini()# purbeurre data base initialisation
	database.table_products()# Product table initialisation
	database.table_categories()# Categories table initialisation
	database.table_backup()# Backup table initialisation

	#Database filling
	filling.built_data_products()# Filling Products table with Open Food Facts database
	filling.build_data_categories()# Filling Categories table with Open Food Facts database