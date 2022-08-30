from conections import session
from models import Users
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException
import bcrypt
import jwt
from dotenv import load_dotenv
import os 

load_dotenv()


def CreateUser(newUser, newPassword):
    hashPassword = bcrypt.hashpw(newPassword.encode('utf8'), bcrypt.gensalt(rounds=10))
    newClient = Users(username=newUser, password=hashPassword.decode('utf8'))
    session.add(newClient)
    session.commit()
    return 'se agrego un nuevo usuario'

def DeleteUser(form_data: OAuth2PasswordRequestForm = Depends()):
    client = session.query(Users).filter(Users.username == form_data.username).first()
    hashpwdclient = bcrypt.checkpw(form_data.password.encode('utf8'), client.password.encode('utf8'))
    if hashpwdclient:
        session.delete(client)
        session.commit()
        return 'se elimino un usuario'
    else: 
        return 'no tenes permitido hacer eso'
 


def ChangePassword(form_data: OAuth2PasswordRequestForm = Depends()):
    client = session.query(Users).filter(Users.username == form_data.username).first()
    hashpwdclient = bcrypt.checkpw(form_data.password.encode('utf8'), client.password.encode('utf8'))
    if hashpwdclient:
        changepwd = session.query(Users.username == form_data.username).update(Users.password == form_data.newPassword)
        session.commit(changepwd)
        return 'se cambio el password'
    else: 
        return 'no tenes permitido hacer eso'


def Login(form_data: OAuth2PasswordRequestForm = Depends()):
    client = session.query(Users).filter(Users.username == form_data.username).first()
    if client is not None:
        hashpwdclient = bcrypt.checkpw(form_data.password.encode('utf8'), client.password.encode('utf8'))
        if hashpwdclient:
            payload = {'name': client.username, 'admin': client.admin}
            token = jwt.encode(payload, os.getenv('jwtkey'), algorithm="HS256")
            return token
    raise HTTPException(status_code=400, detail="Incorrect username or password")


def CheckToken(token):
    try:
        data = jwt.decode(token, os.getenv('jwtkey'), algorithm=["HS256"])
        return 'esta pagina es privada'
    except:
        return 'hubo un fallo'


def CheckAdmin(token):
    try:
        data = jwt.decode(token, os.getenv('jwtkey'), algorithm=["HS256"])
        print(bool(data['admin']))
        if bool(data['admin']) == True:
            return 'sos admin pa'
    except:
        return 'no sos admin peton'
        
