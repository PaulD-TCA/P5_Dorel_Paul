#! /usr/bin/env python3
# coding: utf-8

import requests
import mysql.connector
from mysql.connector import errorcode


class DatabaseIni:

    """
    Database initialization
      1. Initialize Pur Beurre database.
      2. Initialize tables.
    """

    def db_ini(self, user_data, mysql_queries):
        """
        Database initialisation
        @return:
          1. Delete a former database.
          2. Create a new Mysql database.
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
                        (host, user, password and database name)
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        """
        mysql_login = mysql.connector.connect(**user_data.DATA)
        cursor = mysql_login.cursor()
        cursor.execute(mysql_queries.DROP_DB)
        cursor.execute(mysql_queries.CREATE_DB)
        cursor.close()
        mysql_login.close()

    def tables_initialization(self, user_data, mysql_queries):
        """
        Tables initialization
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        @return: Create tables with instructions from MySQL instructions.
          stored in a file "mysql_queries" If tables are here already, the
          sript will print "already exist". Else the scrip will print "OK"
        """
        cnx = mysql.connector.connect(**user_data.DATA)
        cursor = cnx.cursor()
        for table_name in mysql_queries.TABLES:
            table_description = mysql_queries.TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        cursor.close()
        cnx.close()
