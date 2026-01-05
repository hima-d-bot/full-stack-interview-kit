import { useState, useEffect } from 'react';

export const useTasks = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/tasks')
      .then(res => res.json())
      .then(data => {
        // BUG: Backend returns {items: []}, frontend expects {data: []}
        setTasks(data.data || []);
        setLoading(false);
      });
  }, []);

  return { tasks, loading };
};
