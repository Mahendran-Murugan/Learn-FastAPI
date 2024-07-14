from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Mahendran Murugan Learning FastAPI",
    description="To test fastapi implementation and decide it is suitable for projects",
    version="0.0.1"
)

class Details(BaseModel):
    """Basic Syntax of Details

    Args:
        BaseModel (_type_): _description_
    """
    name: str = Field(description="Name of a Person")
    age: int = Field(description="Age of a Person")
    status: str = Field(description="Status of a Person")
    
@app.get("/",
         responses={
             404: {"description":"Person not Found"},
             400: {"description":"Error Occured"}
         })
def getDetails():
    return Details(name="Mahendran", age=19, status="Single")