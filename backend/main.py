from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [ # list of tasks
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Learn FastAPI", "completed": False}
]



@app.get("/")
async def root():
    return {"message": "Hello FASTAPI"}

@app.get("/tasks") # retrieve a list with data
def get_tasks():
    return tasks
class TaskCreate(BaseModel):
    title:str



# create new task and add it to the tasks list
@app.post("/tasks")
def create_tasks(task:TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }
    tasks.append(new_task)
    return new_task

# Get the task with its unique ID
@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    for task in tasks:
        if task["id"]== task_id:
            return task
        
    raise HTTPException(status_code = 404, detail="Task with this ID doesnt exists" )

# Delete the task by finding the ID and removing it 
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
             tasks.remove(task)
             return {"message": "Task Deleted"}
        
        
    raise HTTPException(status_code = 404, detail="Task with this ID alreayd deleted" )    
