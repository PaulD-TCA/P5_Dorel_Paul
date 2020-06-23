#! /usr/bin/env python3
# coding: utf-8


from PBAppliModules import pb_main_loop
from PBAppliModules import user_choice
from PBAppliModules import pbeurre_screen1
from PBAppliModules import pbeurre_screen2
from PBAppliModules import pbeurre_screen3
#from PBAppliModules import constants



def main():
	"""
	Main file. Make instances and activate the main loop.
	  - sc1 : display the welcome screen and the backup screen
	  - sc2 : display the categories screen and results of the junk food query
	  - sc3 : display a substitution product and save it
	"""
	#Instance creation
	sc1 = pbeurre_screen1.Screen1()
	sc2 = pbeurre_screen2.Screen2()
	uc = user_choice.UserChoice()
	appli_initialisation = pb_main_loop.AppliManagement()
	sc3 = pbeurre_screen3.Screen3()

	#Main loop activation
	appli_initialisation.appli_main_loop(sc1, sc2, sc3, uc)

if __name__ == "__main__":
	main()
