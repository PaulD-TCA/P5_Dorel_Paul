#! /usr/bin/env python3
# coding: utf-8

import mysql.connector

#modules import

#from PBAppliModules import PBeurre_Screen1, PBeurre_Screen2, PBeurre_Screen3, constants
from PBAppliModules import mysql_queries, user_data, constants
from PBAppliModules import pbeurre_screen1
from PBAppliModules import pbeurre_screen2

class AppliManagement:#pb_main_loop
#    def __init__(self):

#        self.cnx = mysql.connector.connect(user = user_data.DATA["user"],
#                                        password = user_data.DATA["password"],
#                                        host = user_data.DATA["host"],
#                                        database = constants.DB_NAME)
#        self.cursor = self.cnx.cursor()


    def appli_main_loop(self, sc1, sc2, sc3):
        #Instances creation

        appli_running = "on"
        while appli_running == "on":
            sc1.welcome(constants)
            if sc1.user_choice_welcome == "1":
                sc2.categories_display(constants)
                sc2.lookforproducts(mysql_queries, constants)
#                print("mainloop"+sc2.result_for_substitution)
                sc2.substitution(mysql_queries, constants)

            else:
                appli_running = "off"
            continue
