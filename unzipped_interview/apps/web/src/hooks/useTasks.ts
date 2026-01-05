import { useState, useEffect } from 'react';

export interface Task {
  id: number;
  title: string;
  description: string;
  status: string;
  created_at: string;
  updated_at: string;
}

export const useTasks = (page: number, limit: number, status?: string) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);

  // BUG: Missing useCallback - this function is recreated on every render
  const fetchTasks = async () => {
    setLoading(true);
    try {
      const url = new URL('/api/tasks', window.location.origin);
      url.searchParams.append('page', page.toString());
      url.searchParams.append('limit', limit.toString());
      if (status) url.searchParams.append('status', status);

      const response = await fetch(url.toString());
      const result = await response.json();
      
      // BUG: Integration mismatch - Frontend expects 'data' but Backend sends 'items'
      // This will cause 'tasks' to be undefined/empty
      setTasks(result.data); 
      setTotal(result.total);
    } catch (error) {
      console.error('Failed to fetch tasks', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
    // BUG: Missing dependencies in useEffect
  }, []); 

  return { tasks, total, loading, refetch: fetchTasks };
};
