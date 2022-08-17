from fastapi import FastAPI
from functions import CreateUser, CheckUser

app = FastAPI()

@app.get('/')
def index():
    return 'hola'

@app.post('/newuser')
def createtest(newUser, newPassword):
    return CreateUser(newUser, newPassword)

@app.get('/checkuser')
def checktest(user, password):
    return CheckUser(user, password)