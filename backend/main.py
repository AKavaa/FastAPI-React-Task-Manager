from fastapi import FastAPI
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

