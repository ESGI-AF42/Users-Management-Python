from corp import Corp
class Member(Corp):

    def __init__(self, Name, Firstname, Age, Post, Phone, Email, Login, Password):
        self.name = Name
        self.firstname = Firstname
        self.age = Age
        self.post = Post
        self.phone = Phone
        self.email = Email
        self.login = Login
        self.password = Password

    def get_entreprise_name(self):
        return self.name

    def get_entreprise_firstname(self):
        return self.firstname
    
    def get_entreprise_age(self):
        return self.age

    def get_entreprise_post(self):
        return self.post

    def get_entreprise_phone(self):
        return self.phone

    def get_entreprise_email(self):
        return self.email
    
    def get_entreprise_login(self):
        return self.login

    def get_entreprise_password(self):
        return self.password
