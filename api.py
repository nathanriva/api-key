from fastapi import FastAPI

app = FastAPI()

@app.get('/public')
def public():
    return 'public'

@app.get('/private')
def private():
    return 'response'