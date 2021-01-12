class User:
    def __init__(self, username, password, email, fullname):
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname

    def reset_password(self,password):
        self.password = 'new_password'
        return password

    def change_name(self, fullname):
        self.fullname = 'enter fullname'
        return fullname

    def change_login(self,email):
        self.email = 'enter new email'
        return email

    def change_username(self,username):
        self.username = 'enter the new username'
        return username
