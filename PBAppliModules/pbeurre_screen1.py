#! /usr/bin/env python3
# coding: utf-8

import mysql.connector

class Screen1:
    def __init__(self):

        self.user_choice_welcome = 0

    def welcome(self,constants):

        print(constants.PB_HEADER_DISPLAY)
        print(constants.PB_WELCOME_DISPLAY)
        print(constants.PB_FOOTER_DISPLAY)
#        print("first"+self.user_choice_welcome)


        self.user_choice_welcome = input()
#        print("second"+self.user_choice_welcome)

#        print(self.user_choice_welcome)
