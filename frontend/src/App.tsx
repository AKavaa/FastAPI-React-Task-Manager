import { useEffect, useState } from 'react'

type Task = {
  id: number,
  title: string,
  completed: boolean
}

const App = () => {
  const [tasks, setTasks] = useState<Task[]>([]) // Task Array will return the tasks
  const [title, setTitle]: any = useState("")


  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/tasks');

        // Check if the response is okay (status 200-299)
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data: Task[] = await response.json();
        setTasks(data); // Update your state
      } catch (error) {
        console.error("Failed to fetch tasks:", error);
      }
    };

    fetchTasks();
  }, []);

  const createTask = async () => {

    if (!title) return

    try {
      const response = await fetch('http://127.0.0.1:8000/tasks', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          title: title
        })
      })

      const newTask = await response.json()


      setTasks([...tasks, newTask])


      setTitle("")

    } catch (error) {
      console.error(error)
    }
  }

  const deleteTask = async (id: number) => {
    try {
      await fetch(`http://127.0.0.1:8000/tasks/${id}`, { method: "DELETE" });
      setTasks(tasks.filter(task => task.id !== id));
    } catch (error) {
      console.error("Delete failed", error);
    }
  };



  return (
    <div>
      <h1>Tasks</h1>
      <input type="text" placeholder="Enter a task" value={title} onChange={(e) => setTitle(e.target.value)} />
      <button onClick={createTask}> Add Task</button>

      {tasks.map((task) => (
        <div key={task.id}>
          <p>{task.title}</p>
          <p>{task.completed ? "✅ Completed" : "❌ Not Done"} </p>
          <button onClick={() => deleteTask(task.id)}>Delete Task</button>
        </div>


      ))}</div>
  )
}


export default App;