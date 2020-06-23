#! /usr/bin/env python3
# coding: utf-8

import mysql.connector

from PBAppliModules import constants
from PBAppliModules import user_data
from PBAppliModules import mysql_queries

class AppliManagement:

    """
    Manage the program flow.
    """

    def appli_main_loop(self, sc1, sc2, sc3, uc):
        """
        Mains loop who display each screens following user choises:
        @type sc1: class instance
        @param sc1: Display the welcome screen and the backup screen.
        @type sc2: class instance
        @param sc2: Display the categories screen and results of
                    the junk food query.
        @type sc3: class instance
        @param sc3: Display a substitution product and save it.
        @type uc: class instance
        @param: uc: Force the user to type a number in the choice liste only and
                    memorize user choices.
        @return: The loop will continue until the user close the program.
        """
        appli_running = "on"
        while appli_running == "on":
            sc1.welcome(constants, uc)
            if uc.user_entry == "1":
                sc2.categories_display(constants, uc)
                sc2.lookforproducts(constants, user_data, mysql_queries, uc)
                sc3.substitution(constants, user_data, mysql_queries, sc2, uc)
                if uc.user_entry == "1":
                    sc3.substitution_backup(constants, user_data, mysql_queries)
                elif uc.user_entry == "2":
                    continue
                elif uc.user_entry == "3":
                    appli_running = "off"
            elif uc.user_entry == "2":
                sc1.backup_display(constants, user_data, mysql_queries)
            elif uc.user_entry == "3":
                appli_running = "off"
            continue
