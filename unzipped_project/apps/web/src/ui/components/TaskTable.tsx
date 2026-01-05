import React from 'react';

export const TaskTable = ({ tasks }) => {
  const handleSort = () => {
    // BUG: Mutating state array in-place
    tasks.sort((a, b) => a.title.localeCompare(b.title));
  };

  return (
    <table className="min-w-full">
      <thead>
        <tr>
          <th onClick={handleSort} className="cursor-pointer">Title</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {tasks.map(task => (
          <tr key={task.id}>
            <td>{task.title}</td>
            <td>{task.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
