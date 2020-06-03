#! /usr/bin/env python3
# coding: utf-8

import mysql.connector

#modules import
from PBAppliModules import PBeurre_Screen1, PBeurre_Screen2, PBeurre_Screen3, constants
from PBAppliModules import MYSQL_QUERIES

if __name__ == '__main__':
	#Instances creation
	sc1 = PBeurre_Screen1.Screen1(constants)
	sc2 = PBeurre_Screen2.Screen2(constants)
	sc3 = PBeurre_Screen3.Screen3(constants)


#	sc1.welcome()
#	sc1.categories_screen()
#	sc2.lookforproducts(MYSQL_QUERIES)
	sc3.substitution(MYSQL_QUERIES)
