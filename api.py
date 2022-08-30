from fastapi import FastAPI, Depends
from functions import CreateUser, Login, CheckToken, CheckAdmin, DeleteUser
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=('login'))

@app.post('/newuser')
def createtest(newUser, newPassword):
    return CreateUser(newUser, newPassword)

@app.delete('/delete')
def Delete(form_data: OAuth2PasswordRequestForm = Depends()):
    return DeleteUser(form_data)

@app.post('/login')
def auth(form_data: OAuth2PasswordRequestForm = Depends()):
    return Login(form_data)

@app.get('/priv')
def auth2(token):
    return CheckToken(token)

@app.get('/admins')
def admins(token):
    return CheckAdmin(token)
