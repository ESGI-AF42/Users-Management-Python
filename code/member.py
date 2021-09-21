
class Member():

    def __init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID):
        self.name = UserName
        self.firstname = UserFirstname
        self.age = Age
        self.phone = Phone
        self.email = Email
        self.login = Login
        self.password = hash(Password)
        self.corp_id = CorpID
        self.level = ""

    def get_member_name(self):
        return self.name

    def get_member_firstname(self):
        return self.firstname
    
    def get_member_age(self):
        return self.age


    def get_member_phone(self):
        return self.phone

    def get_member_email(self):
        return self.email
    
    def get_member_login(self):
        return self.login

    def get_member_password(self):
        return self.password

    def get_member_level(self):
        return self.level

    def set_member_level(self,Level):
        self.level = Level
