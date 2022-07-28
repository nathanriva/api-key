from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def public():
    return 'public'

@app.get('/')
def private():
    return 'private'