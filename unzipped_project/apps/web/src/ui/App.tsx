import React from 'react';
import { TaskTable } from './components/TaskTable';
import { useTasks } from '../hooks/useTasks';

export const App = () => {
  const { tasks, loading } = useTasks();
  
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Task Management</h1>
      {loading ? <p>Loading...</p> : <TaskTable tasks={tasks} />}
    </div>
  );
};
