import React, { useState } from 'react';

export const TaskTable = ({ tasks }) => {
  const [sortKey, setSortKey] = useState('id');

  const handleSort = (key) => {
    setSortKey(key);
    tasks.sort((a, b) => {
      if (typeof a[key] === 'string') {
        return a[key].localeCompare(b[key]);
      }
      return a[key] - b[key];
    });
  };

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-left border-collapse">
        <thead>
          <tr className="bg-gray-50 border-b">
            <th onClick={() => handleSort('id')} className="p-4 cursor-pointer hover:bg-gray-100">ID</th>
            <th onClick={() => handleSort('title')} className="p-4 cursor-pointer hover:bg-gray-100">Title</th>
            <th onClick={() => handleSort('status')} className="p-4 cursor-pointer hover:bg-gray-100">Status</th>
            <th className="p-4">Created</th>
            <th className="p-4 text-right">Actions</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map(task => (
            <tr key={task.id} className="border-b hover:bg-gray-50 transition-colors">
              <td className="p-4 text-gray-500">#{task.id}</td>
              <td className="p-4 font-medium">{task.title}</td>
              <td className="p-4">
                <span className={`px-2 py-1 rounded-full text-xs ${
                  task.status === 'open' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                }`}>
                  {task.status}
                </span>
              </td>
              <td className="p-4 text-sm text-gray-500">
                {new Date(task.created_at).toLocaleDateString()}
              </td>
              <td className="p-4 text-right">
                <button className="text-blue-600 hover:underline mr-3">Edit</button>
                <button className="text-red-600 hover:underline">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
