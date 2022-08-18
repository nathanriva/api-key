from smtplib import bCRLF
from conections import session
from models import Users
import bcrypt

def CreateUser(newUser, newPassword):
    hashPassword = bcrypt.hashpw(newPassword.encode('utf8'), bcrypt.gensalt(rounds=10))
    newClient = Users(username=newUser, password=hashPassword.decode('utf8'))
    session.add(newClient)
    session.commit()
    return 'se a agregado un nuevo usuario'

def CheckUser(user, password):
    client = session.query(Users).filter(Users.username == user).first()
    if (client is not None):
        hashpwdclient = bcrypt.checkpw(password.encode('utf8'), client.password.encode('utf8'))
        if (hashpwdclient):
            return 'pasas'
    return 'usario o contraseña es incorrecto'  
