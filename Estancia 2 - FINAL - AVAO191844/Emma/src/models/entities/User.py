from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, apellido="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.apellido = apellido
        

    @classmethod
    def check_password(self, hashed_password, contra):
        return check_password_hash(hashed_password,contra)

##print(generate_password_hash("Emmanuel0401"))