from fastapi import FastAPI

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

@app.post("/tasks")
def create_tasks(title:str):
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    return new_task