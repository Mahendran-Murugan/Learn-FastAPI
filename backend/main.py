from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from configrations import collection
from database.schema import get_all_todo
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime

app = FastAPI()

origins = ["http://localhost:3000",
           "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

router = APIRouter(prefix="/api")

@router.get('/')
async def get_todos():
    data = collection.find()
    return get_all_todo(data)

@router.post('/')
async def post_todo(todo: Todo):
    try:
        res = collection.insert_one(dict(todo))
        return {"status":200, "id":str(res.inserted_id)} 
    except Exception as e:
        return HTTPException(status_code=400, detail=f"Exception Occured {e}")
    
@router.put('/{todo_id}')
async def update_todo(todo_id:str, updated_todo: Todo):
    try:
        id = ObjectId(todo_id)
        todo = collection.find_one({"_id":id, "is_deleted":False})
        if not todo:
            return HTTPException(status_code=404, detail=f"Task doesn't Exisit")
        updated_todo.updated = int(datetime.timestamp(datetime.now()))
        res = collection.update_one({"_id":id}, {"$set":dict(updated_todo)})
        return {"status":200, "message":f"updating todo {todo_id} was successful"}
    except Exception as e:
        return HTTPException(status_code=400, detail=f"Exception Occured {e}")
    
@router.delete('/{todo_id}')
async def delete_todo(todo_id:str):
    try:
        id = ObjectId(todo_id)
        todo = collection.find_one({"_id":id, "is_deleted":False})
        if not todo:
            return HTTPException(status_code=404, detail=f"Task doesn't Exisit")
        deleted_todo = collection.delete_one({"_id":id})
        return {"status":200, "message":f"deleting todo {todo_id} was successful"}
    except Exception as e:
        return HTTPException(status_code=400, detail=f"Exception Occured {e}")

app.include_router(router)