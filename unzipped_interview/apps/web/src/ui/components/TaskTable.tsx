import React, { useState } from 'react';
import { Task } from '../../hooks/useTasks';

interface TaskTableProps {
  tasks: Task[];
  loading: boolean;
}

export const TaskTable: React.FC<TaskTableProps> = ({ tasks, loading }) => {
  const [sortField, setSortField] = useState<keyof Task>('id');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc');

  // BUG: State mutation in-place
  // tasks.sort() mutates the original array which is part of the state/props
  const sortedTasks = tasks.sort((a, b) => {
    const aValue = a[sortField];
    const bValue = b[sortField];
    if (aValue < bValue) return sortOrder === 'asc' ? -1 : 1;
    if (aValue > bValue) return sortOrder === 'asc' ? 1 : -1;
    return 0;
  });

  const handleSort = (field: keyof Task) => {
    if (field === sortField) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(field);
      setSortOrder('asc');
    }
  };

  if (loading) return <div>Loading tasks...</div>;

  return (
    <table className="min-w-full divide-y divide-gray-200">
      <thead className="bg-gray-50">
        <tr>
          <th onClick={() => handleSort('id')} className="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
          <th onClick={() => handleSort('title')} className="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
          <th onClick={() => handleSort('status')} className="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
          <th onClick={() => handleSort('created_at')} className="cursor-pointer px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Created At</th>
        </tr>
      </thead>
      <tbody className="bg-white divide-y divide-gray-200">
        {sortedTasks.map((task) => (
          <tr key={task.id}>
            <td className="px-6 py-4 whitespace-nowrap">{task.id}</td>
            <td className="px-6 py-4 whitespace-nowrap">{task.title}</td>
            <td className="px-6 py-4 whitespace-nowrap">{task.status}</td>
            <td className="px-6 py-4 whitespace-nowrap">{new Date(task.created_at).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
