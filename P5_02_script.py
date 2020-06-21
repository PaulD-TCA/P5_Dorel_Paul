#! /usr/bin/env python3
# coding: utf-8


import json
import requests
import mysql.connector

#modules import
from PBAppliModules import database_initialization
from PBAppliModules import database_filling
from PBAppliModules import mysql_queries
from PBAppliModules import constants
from PBAppliModules import user_data


def main():
    """
    Main file who generate the data base "Pur Beurre".
      1. Data base initialization.
         - a data base named "purbeurredb" is initialized.
         - 3 tables are initialized.
      2. Data base filling.
         - Table "Products".
         - Table "Categories".
    """
    #Instances creation
    database = database_initialization.DatabaseIni()
    filling = database_filling.DatabaseFill()

    #Data base initialisation
    database.db_ini(user_data, mysql_queries)
    database.tables_initialization(user_data, mysql_queries)

    #Database filling
    filling.built_data_products(constants, user_data, mysql_queries)
    filling.build_data_categories(constants, user_data, mysql_queries)
    print("Data base is done")


if __name__ == '__main__':
	main()
