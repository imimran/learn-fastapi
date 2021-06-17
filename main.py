from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return { 'data': {"msg": "Hello World"}}


@app.get("/about")

def index():
    return { 'data': {"msg": "About Page"}}