# Written by Aidan Coyne

class UserProfile:
    def __init__(self):
        self.country = ""
        self.description = ""
        self.profile_picture = bytearray()

    def edit_description(self, new_description):
        self.description = new_description

    def edit_picture(self, new_pic):
        self.profile_picture = bytearray(new_pic)

    def edit_country(self, new_country):
        self.country = new_country
