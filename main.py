from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Details(BaseModel):
    name: str
    age: int
    status: str
    
@app.get("/")
def getDetails():
    return Details(name="Mahendran", age=19, status="Single")