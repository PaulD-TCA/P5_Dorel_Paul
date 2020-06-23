#! /usr/bin/env python3
# coding: utf-8

import mysql.connector

class Screen1:

    """
    Display the welcome screen and the backup screen.
    """

    def welcome(self,constants,uc):

        """
        Display the welcome screen.
        @type constant: string
        @param constant: Parts of the text to show.
        @type uc: class instance
        @param uc: Force the user to type a number in the choice liste only and
                    memorize user choices.
        @return: the user choice in the list 
        """

        print(constants.PB_HEADER_DISPLAY)
        print(constants.PB_WELCOME_DISPLAY)
        print(constants.PB_FOOTER_DISPLAY)
        uc.user_choice(3)

    def backup_display(self,constants, user_data, mysql_queries):
        """
        Display the backup screen.
        @type constant: string
        @param constant: Parts of the text to show.
        @type user_data: dictionary
        @param user_data: contain user datas for connextion to the database
                        (host, user, password and database name)
        @type mysql_queries: string
        @param mysql_queries: SQL queries used with mysql connector.
        @return: null
        """
        cnx = mysql.connector.connect(**user_data.DATA)
        cursor = cnx.cursor()
        cursor.execute(mysql_queries.BACKUP_DISPLAY)
        print(constants.PB_HEADER_DISPLAY)
        for (p_name, b_date, p_url) in cursor:
            print("{}.\nRecherché le {:%d %b %Y}\n{}\n".format(p_name, b_date, p_url))
        print(constants.PB_FOOTER_DISPLAY)
        input("Appuyez sur entrer pour continuer")
