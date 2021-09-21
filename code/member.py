from corp import Corp
class Member(Corp):

    def __init__(self, Name, Firstname, Age, Phone, Email, Login, Password):
        self.name = Name
        self.firstname = Firstname
        self.age = Age
        self.phone = Phone
        self.email = Email
        self.login = Login
        self.password = Password

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
