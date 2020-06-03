#! /usr/bin/env python3
# coding: utf-8

import mysql.connector
#from mysql.connector import errorcode

DB_NAME = 'pbdatabase'

TABLES = {}

TABLES['Products'] = (
    "CREATE TABLE `Products` ("
    "  `p_id` int unsigned NOT NULL AUTO_INCREMENT,"
    "  `p_code` varchar(50),"
    "  `p_name` varchar(200),"
    "  `p_nutrition_grade_fr` text(1),"
    "  `p_ingredients_text` varchar(2000),"
    "  `p_store` varchar(200),"
    "  `p_compared_to_category` varchar(200),"
    "  `p_categories_tags` varchar(5000),"
    "  `p_url` varchar(1000),"
    "  `p_category_three` varchar(500),"
    "  `categories_id` tinyint(3),"
    "  PRIMARY KEY (`p_id`)"
    ") ENGINE=InnoDB")

TABLES['Categories'] = (
    "CREATE TABLE `Categories` ("
    "  `c_id` int unsigned NOT NULL AUTO_INCREMENT,"
    "  `c_name` varchar(100),"
    "  PRIMARY KEY (`c_id`)"
    ") ENGINE=InnoDB")

TABLES['Backup'] = (
    "CREATE TABLE `Backup` ("
    "  `b_id` int unsigned NOT NULL AUTO_INCREMENT,"
    "  `b_date` date,"
    "  `products_id` int,"
    "  PRIMARY KEY (`b_id`)"
    ") ENGINE=InnoDB")

DATA_PRODUCTS = ("INSERT INTO Products "
                "(p_code, p_name, p_nutrition_grade_fr, p_ingredients_text,"
                " p_store, p_compared_to_category, p_categories_tags, p_url,"
                " categories_id) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

DATA_CATEGORIES = ("INSERT IGNORE INTO Categories "
                    "(c_id, c_name) "
                    "VALUES (%(c_idtofill)s, %(categorie)s)")

QUERY = ("SELECT p_name, p_nutrition_grade_fr, p_categories_tags FROM Products "
        "WHERE categories_id = 2 AND (p_nutrition_grade_fr = 'D' OR p_nutrition_grade_fr = 'E')")

QUERY2 = ("SELECT p_id, categories_id, p_nutrition_grade_fr, p_name FROM Products "
        "WHERE p_categories_tags LIKE '%en:prepared-meats%' AND (p_nutrition_grade_fr = 'A' OR p_nutrition_grade_fr = 'B')")
