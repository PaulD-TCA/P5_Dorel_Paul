#! /usr/bin/env python3
# coding: utf-8

import random
import datetime

import mysql.connector


class Screen3:

    """
    Display a substitution product.
    """
    def __init__(self):

        self.product_id_backup = ""


    def substitution(self, constants, user_data, mysql_queries, sc2, uc):
        """
        Display a substitution product.
        @type constant: string
        @param constant: Parts of the text to show.
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
                        (host, user, password and database name)
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        @type sc2: string
        @param sc2:
        @type uc: class instance
        @param uc: Force the user to type a number in the choice liste only and
                    memorize user choices.
        @return: the user choice in the list and the product id
        """
        categories_list = (list(sc2.res_substi.split(",")))
        categories_list.reverse()
        result_query_healthy_food = []
        smaller_list = []
        for each_tag in categories_list:
            each_tag = "%"+each_tag+"%"
            print(each_tag)
            cnx = mysql.connector.connect(**user_data.DATA)
            cursor = cnx.cursor()
            cursor.execute(mysql_queries.HEALTHY_FOOD, (each_tag,))
            list_healthy_food = []

            for each_food in cursor:
                list_healthy_food.append(each_food)
            quantity_list = (len(list_healthy_food))
            print(quantity_list)
            if quantity_list == 0:
                quantity_list = 10000
            smaller_list.append(quantity_list)
            result_query_healthy_food.append(list_healthy_food)
        min_index = smaller_list.index(min(smaller_list))
        hf_choice = random.choices(result_query_healthy_food[min_index])
        print(constants.PB_HEADER_DISPLAY)
        print(constants.PB_PROPOSITION_HF_DISPLAY)
        print("       "+hf_choice[0][1]+"\n")
        print("       Score nutritionnel: "+hf_choice[0][2]+"\n")
        print("       La composition de ce produit est: "+hf_choice[0][3]+"\n")
        print("       Vous pourriez trouver ce produit: "+hf_choice[0][4]+"\n")
        print("       Pour plus d'information suivez ce lien: "+hf_choice[0][5])
        print(constants.PB_SUBSTITUTION_DISPLAY)
        print(constants.PB_FOOTER_DISPLAY)
        uc.user_choice(3)
        self.product_id_backup = hf_choice[0][0]

    def substitution_backup(self, constants, user_data, mysql_queries):
        """
        Save the substitution result.
        @type constant: string
        @param constant: Parts of the text to show.
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
                        (host, user, password and database name)
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        @return: write the prduct id and the current date in backup table
        """
        date_query = datetime.datetime.today()
        backup_data = {'b_date': date_query,
        'products_id': self.product_id_backup}
        cnx = mysql.connector.connect(**user_data.DATA)
        cursor = cnx.cursor()
        cursor.execute(mysql_queries.QUERY_BACKUP, backup_data)
        cnx.commit()
