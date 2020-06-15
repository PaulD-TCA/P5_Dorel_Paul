#! /usr/bin/env python3
# coding: utf-8

TABLES = {}

TABLES['Products'] = (
    "CREATE TABLE `Products` ("
    "  `p_id` int unsigned NOT NULL AUTO_INCREMENT,"
    "  `p_code` varchar(50),"
    "  `p_name` varchar(200),"
    "  `p_nutrition_grade_fr` text(1),"
    "  `p_ingredients_text` varchar(2000),"
    "  `p_store` varchar(200),"
    "  `p_categories_tags` varchar(1000),"
    "  `p_categories_hierarchy` varchar(1000),"
    "  `p_url` varchar(1000),"
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
                " p_store, p_categories_tags, p_categories_hierarchy, p_url,"
                " categories_id) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

DATA_CATEGORIES = ("INSERT IGNORE INTO Categories "
                    "(c_id, c_name) "
                    "VALUES (%(c_idtofill)s, %(categorie)s)")

JUNCK_FOOD = ("SELECT p_name, p_nutrition_grade_fr, p_categories_hierarchy "
            "FROM Products "
            "WHERE categories_id = %s "
            "AND (p_nutrition_grade_fr = 'D' "
            "OR p_nutrition_grade_fr = 'E')")

HEALTHY_FOOD = ("SELECT p_id, p_name, p_nutrition_grade_fr, "
                "p_ingredients_text, p_store, p_url FROM Products "
                "WHERE p_categories_hierarchy LIKE %s "
                "AND (p_nutrition_grade_fr = 'A' "
                "OR p_nutrition_grade_fr = 'B')")

QUERY_BACKUP = ("INSERT IGNORE INTO Backup "
                "(b_date, products_id) "
                "VALUES (%(b_date)s, %(products_id)s)")

BACKUP_DISPLAY = ("SELECT Products.p_name, Backup.b_date, Products.p_url "
                "FROM Products "
                "INNER JOIN Backup ON Products.p_id = Backup.products_id")
