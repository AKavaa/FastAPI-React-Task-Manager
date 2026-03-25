from fastapi import FastAPI

app = FastAPI()

tasks = [ # list of tasks
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Learn FastAPI", "completed": False}
]

@app.get("/")
async def root():
    return {"message": "Hello FASTAPI"}

@app.get("/tasks")
def get_tasks():
    return tasks