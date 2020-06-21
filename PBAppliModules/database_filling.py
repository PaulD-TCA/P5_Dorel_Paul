#! /usr/bin/env python3
# coding: utf-8

import json
import requests
import mysql.connector

class DatabaseFill:

    """
    Fill "Pur Beurre" database with data taken from
    Open Food Facts API and data from "constants" file.
    """

    def built_data_products(self,constants, user_data, mysql_queries):
        """
        Fill the table "Products" with datas from Open Food Facts API.
        @type constant: string
        @param constant: Parts of the text to show.
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
                        (host, user, password and database name)
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        @return:
          1. Get a JSON file from API.
          2. Read the JSON file.
          3. Product by product we get the wanted data. If data are missing we
          go to the next product.
          4. Store data in the table.
        """
        cnx = mysql.connector.connect(**user_data.DATA)
        cursor = cnx.cursor()
        for categorie in constants.CATEGORIES:
            categories_id = constants.CATEGORIES.index(categorie)+1
            for nutrition_grade in constants.NUTRITION_GRADES:
                resp = requests.get(constants.URL_PART_1+categorie+
                    constants.URL_PART_2+nutrition_grade+constants.URL_PART_3)
                data = resp.json()
                nb_prods = int(data["count"])
                page_s = int(data["page_size"])
                row_w = 0
                p_id = 1
                if page_s <= nb_prods:
                    maxproduct = page_s
                else:
                    maxproduct = nb_prods
                while row_w < maxproduct:
                    try:
                        p_id = p_id + 1
                        p_code = data["products"][row_w]["code"]
                        p_name = data["products"][row_w]["product_name"]
                        p_name = p_name.replace('"', "'")
                        p_nut_gr = data["products"][row_w]["nutrition_grade_fr"]
                        p_ingre_t = data["products"][row_w]["ingredients_text"]
                        p_store = data["products"][row_w]["stores"]
                        p_ca_tags = data["products"][row_w]["categories_tags"]
                        p_ca_tags = str.join(",",p_ca_tags)
                        p_ca_h = data["products"][row_w]["categories_tags"]
                        p_ca_h = str.join(",",p_ca_h)
                        p_url = constants.URL_OPEN_FOOD_FACTS + p_code
                        row_w = row_w + 1
                        data_prod =(p_code, p_name, p_nut_gr, p_ingre_t,
                                    p_store, p_ca_tags, p_url, categories_id)
                        cursor.execute(mysql_queries.DATA_PRODUCTS, data_prod)
                        cnx.commit()
                    except:
                        row_w = row_w + 1
            print("Categorie "+categorie+" ok. ("+str(categories_id)+ "/15)")

    def build_data_categories(self,constants, user_data, mysql_queries):
        """
        @type constant: string
        @param constant: Parts of the text to show.
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
                        (host, user, password and database name)
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        @return: Fill the table Categories with a categorie list taken from the file
        "constants".
        """
        cnx = mysql.connector.connect(**user_data.DATA)
        cursor = cnx.cursor()
        c_idtofill = 1
        for categorie in constants.CATEGORIES:
            data_categorie = {
            'c_idtofill': c_idtofill,
            'categorie': categorie
            }
            cursor.execute(mysql_queries.DATA_CATEGORIES, data_categorie)
            c_idtofill = c_idtofill + 1
            cnx.commit()
        cursor.close()
        cnx.close()
