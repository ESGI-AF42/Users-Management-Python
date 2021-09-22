import hashlib, binascii, os


class User():

    def __init__(self, UserName, UserFirstname, Age, Phone, Email, Login, Password, CorpID):
        self.name = UserName
        self.firstname = UserFirstname
        self.age = Age
        self.phone = Phone
        self.email = Email
        self.login = Login
        key = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        psswdHashed = hashlib.pbkdf2_hmac('sha512', Password.encode('utf-8'),key, 100000)
        psswdHashed = binascii.hexlify(psswdHashed)
        self.password = (key + psswdHashed).decode('ascii')
        self.corp_id = CorpID
        self.level = ""

    def get_user_name(self):
        return self.name

    def get_user_firstname(self):
        return self.firstname
    
    def get_user_age(self):
        return self.age

    def get_user_phone(self):
        return self.phone

    def get_user_email(self):
        return self.email
    
    def get_user_login(self):
        return self.login

    def get_user_password(self):
        return self.password

    def get_user_level(self):
        return self.level

    def set_user_level(self,Level):
        self.level = Level

    def verify_psswd(stored_password, provided_password):
        key = stored_password[:64]
        stored_password = stored_password[64:]
        psswdHashed = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), key.encode('ascii'), 100000)
        psswdHashed = binascii.hexlify(psswdHashed).decode('ascii')
        return psswdHashed == stored_password
