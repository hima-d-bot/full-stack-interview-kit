import React, { useState } from 'react';
import { useTasks } from '../hooks/useTasks';
import { TaskTable } from './components/TaskTable';

export const App: React.FC = () => {
  const [page, setPage] = useState(1);
  const [status, setStatus] = useState<string | undefined>(undefined);
  const { tasks, total, loading } = useTasks(page, 10, status);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Task Management</h1>
      
      <div className="mb-4 flex gap-4">
        <select 
          value={status || ''} 
          onChange={(e) => setStatus(e.target.value || undefined)}
          className="border p-2 rounded"
        >
          <option value="">All Statuses</option>
          <option value="open">Open</option>
          <option value="closed">Closed</option>
        </select>
        
        <div className="flex items-center gap-2">
          <button 
            onClick={() => setPage(p => Math.max(1, p - 1))}
            disabled={page === 1}
            className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
          >
            Previous
          </button>
          <span>Page {page}</span>
          <button 
            onClick={() => setPage(p => p + 1)}
            disabled={page * 10 >= total}
            className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
          >
            Next
          </button>
        </div>
      </div>

      <TaskTable tasks={tasks} loading={loading} />
    </div>
  );
};
