import React, { useState } from 'react';
import { TaskTable } from './components/TaskTable';
import { useTasks } from '../hooks/useTasks';

export const App = () => {
  const { tasks, loading, refresh } = useTasks();
  const [view, setView] = useState('list');
  
  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-sm p-4 mb-8">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <h1 className="text-xl font-bold text-gray-800">TaskFlow Pro</h1>
          <div className="space-x-4">
            <button onClick={() => setView('list')} className="text-blue-600">Tasks</button>
            <button onClick={() => setView('stats')} className="text-gray-600">Stats</button>
            <button onClick={refresh} className="bg-blue-600 text-white px-4 py-2 rounded">Refresh</button>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4">
        {loading ? (
          <div className="flex justify-center p-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow">
            <div className="p-6 border-b">
              <h2 className="text-lg font-semibold">Active Tasks ({tasks.length})</h2>
            </div>
            <TaskTable tasks={tasks} />
          </div>
        )}
      </main>
    </div>
  );
};
