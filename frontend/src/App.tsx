import { useEffect, useState } from 'react'

type Task = {
  id: number,
  title: string,
  completed: boolean
}

const App = () => {
  const [tasks, setTasks] = useState<Task[]>([]) // Task Array will return the tasks

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

  return (
    <div>
      <h1>Tasks</h1>
      {tasks.map((task) => (
        <div key={task.id}>
          <p>{task.title}</p>
          <p>{task.completed ? "✅ Completed" : "❌ Not Done"} </p>
        </div>


      ))}</div>
  )
}


export default App;