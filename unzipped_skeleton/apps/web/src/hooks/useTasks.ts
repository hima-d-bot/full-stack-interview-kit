import { useState, useEffect, useCallback } from 'react';

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

  const fetchTasks = useCallback(async () => {
    setLoading(true);
    try {
      const url = new URL('/api/tasks', window.location.origin);
      url.searchParams.append('page', page.toString());
      url.searchParams.append('limit', limit.toString());
      if (status) url.searchParams.append('status', status);

      const response = await fetch(url.toString());
      const result = await response.json();
      // Clean version uses 'data' key
      setTasks(result.data);
      setTotal(result.total);
    } catch (error) {
      console.error('Failed to fetch tasks', error);
    } finally {
      setLoading(false);
    }
  }, [page, limit, status]);

  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  return { tasks, total, loading, refetch: fetchTasks };
};
