def single_todo(todo):
    return {
        "id":str(todo["_id"]),
        "title":str(todo["title"]),
        "description":str(todo["description"]),
        "status":str(todo["status"]),
    }
    
def get_all_todo(todos):
    return [single_todo(todo=todo) for todo in todos]