#! /usr/bin/env python3
# coding: utf-8

import random
import ast
import mysql.connector
import json


class Screen2:

    """
    Display the categories screen and results of the junk food query.
    """

    def __init__(self):
        self.res_substi = 0
        self.categorie_number = ""

    def categories_display(self, constants, uc):
        """
        Display the categories screen.
        @type constant: string
        @param constant: Parts of the text to show.
        @type uc: class instance
        @param uc: Force the user to type a number in the choice liste only and
                    memorize user choices.
        @return: the user choice in the list
        """
        print(constants.PB_HEADER_DISPLAY)
        print(constants.PB_CATEGORIES_DISPLAY)
        for category in constants.CATEGORIES:
            self.categorie_number = constants.CATEGORIES.index(category) + 1
            print("     " + str(self.categorie_number) + "   " + category)
        print(constants.PB_FOOTER_DISPLAY)
        uc.user_choice(self.categorie_number)

    def lookforproducts(self, constants, user_data, mysql_queries, uc):
        """
        Display results of the junk food query
        @type constant: string
        @param constant: Parts of the text to show.
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
                        (host, user, password and database name)
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        @type uc: class instance
        @param: uc: Force the user to type a number in the choice liste only and
                    memorize user choices.
        @return: the user choice in the list and and dictionary with
                 categorie tags of the substitued food
        """
        cnx = mysql.connector.connect(**user_data.DATA)
        cursor = cnx.cursor()
        cursor.execute(mysql_queries.JUNCK_FOOD, (uc.user_entry,))
        list_jf = []
        for raw_list_jf in cursor:
            p_name, p_nutrition_grade_fr, p_categories_tags, = raw_list_jf
            list_jf.append("""p_name": "{}", "p_nutrition_grade_fr": "{}",
             "p_categories_tags": "{}""".format(p_name, p_nutrition_grade_fr,
             p_categories_tags))
        food_to_display = random.choices(list_jf, k=5)
        dicionnary_format = []
        for each_tuple in food_to_display:
            tuple = ("{\""+each_tuple+"\"}")
            tuple = tuple.split('\n')
            tuple = " ".join(tuple)
            dicionnary_format.append(tuple)
        print(constants.PB_HEADER_DISPLAY)
        print(constants.PB_PROPOSITION_JF_DISPLAY)
        junck_food_list_num = 1
        jf_dicio = []
        for list_of_choice in dicionnary_format:
            dicionnary_conversion = ast.literal_eval(list_of_choice)
            print("   "+str(junck_food_list_num)+"   "+
            dicionnary_conversion["p_name"]+".\n       Score nutritionnel: "+
            dicionnary_conversion["p_nutrition_grade_fr"]+"\n")
            junck_food_list_num = junck_food_list_num + 1
            jf_dicio.append(dicionnary_conversion)
        print(constants.PB_FOOTER_DISPLAY)
        uc.user_choice(junck_food_list_num-1)
        user_choice_junck_food = int(uc.user_entry)-1
        self.res_substi = jf_dicio[user_choice_junck_food]["p_categories_tags"]
