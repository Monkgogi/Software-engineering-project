class USERPROFILE:

    def __init__(self,country,description):
        self.__country = country
        self.__description = description

    def __str__(self):
        return str(self.__description)


country = str(input('Enter your country of origin:'))
description = str(input('Enter the reason for you travel and length of days:'))
