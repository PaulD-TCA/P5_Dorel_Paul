#! /usr/bin/env python3
# coding: utf-8

class UserChoice:

    """
    Force the user to type a number in the choice liste only.
    Memorize user choices.
    @type  max: integer
    @return: User choice for program flow
    """

    def __init__(self):
        self.user_entry = ""
    def user_choice(self, max):
        """
        @type  max: integer
        @return: User choice for program flow
        """
        while True:
            self.user_entry = input()
            try:
                if 1 <= int(self.user_entry) <= max:
                    break
                print("Veuillez entrer un numéro de la liste SVP")
            except ValueError:
                print("Veuillez entrer un numéro de la liste SVP")
        return self.user_entry
