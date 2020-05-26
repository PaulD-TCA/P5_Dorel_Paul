#! /usr/bin/env python3
# coding: utf-8


import json
import requests
import mysql.connector

#modules import
from PBAppliModules import database_initialization

if __name__ == '__main__':
	#Instances creation
	database = database_initialization.database_ini()#

	#Data base initialisation
	database.db_ini()# purbeurre data base initialisation
	database.table_products()# Product table initialisation
	database.table_categories()# Categories table initialisation
	database.table_backup()# Backup table initialisation
