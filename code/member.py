import hashlib, binascii, os


class Member():

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

    def verify_psswd(stored_password, provided_password):
        key = stored_password[:64]
        stored_password = stored_password[64:]
        psswdHashed = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), key.encode('ascii'), 100000)
        psswdHashed = binascii.hexlify(psswdHashed).decode('ascii')
        return psswdHashed == stored_password
