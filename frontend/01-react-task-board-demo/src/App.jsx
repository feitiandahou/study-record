import { useState } from 'react';

const INITIAL_TASKS = [
  { id: 1, title: 'Read React component basics', status: 'todo', owner: 'Lin' },
  { id: 2, title: 'Refactor card layout', status: 'doing', owner: 'Mia' },
  { id: 3, title: 'Write deployment notes', status: 'done', owner: 'Kai' },
  { id: 4, title: 'Model API error states', status: 'todo', owner: 'Zoe' },
];

const COLUMNS = [
  { key: 'todo', label: 'Queue', accent: '#c2410c' },
  { key: 'doing', label: 'In Motion', accent: '#0f766e' },
  { key: 'done', label: 'Shipped', accent: '#1d4ed8' },
];

function TaskCard({ task, onStatusChange }) {
  return (
    <article className="task-card">
      <div className="task-meta">
        <span className="task-owner">{task.owner}</span>
        <select value={task.status} onChange={(event) => onStatusChange(task.id, event.target.value)}>
          <option value="todo">todo</option>
          <option value="doing">doing</option>
          <option value="done">done</option>
        </select>
      </div>
      <h3>{task.title}</h3>
    </article>
  );
}

function BoardColumn({ column, tasks, onStatusChange }) {
  return (
    <section className="board-column" style={{ '--accent': column.accent }}>
      <header>
        <p>{column.label}</p>
        <strong>{tasks.length}</strong>
      </header>
      <div className="task-stack">
        {tasks.map((task) => (
          <TaskCard key={task.id} task={task} onStatusChange={onStatusChange} />
        ))}
        {tasks.length === 0 ? <p className="empty-copy">No tasks in this lane.</p> : null}
      </div>
    </section>
  );
}

export default function App() {
  const [tasks, setTasks] = useState(INITIAL_TASKS);

  const stats = {
    total: tasks.length,
    done: tasks.filter((task) => task.status === 'done').length,
    active: tasks.filter((task) => task.status !== 'done').length,
  };

  function handleStatusChange(taskId, nextStatus) {
    setTasks((currentTasks) =>
      currentTasks.map((task) => (task.id === taskId ? { ...task, status: nextStatus } : task)),
    );
  }

  return (
    <main className="task-board-page">
      <section className="hero-panel">
        <div>
          <p className="eyebrow">React Demo 01</p>
          <h1>Task board with local state and live summaries</h1>
          <p className="lead">
            Move tasks across lanes and watch the derived metrics update immediately.
          </p>
        </div>
        <div className="stats-grid">
          <article>
            <span>Total tasks</span>
            <strong>{stats.total}</strong>
          </article>
          <article>
            <span>Active</span>
            <strong>{stats.active}</strong>
          </article>
          <article>
            <span>Done</span>
            <strong>{stats.done}</strong>
          </article>
        </div>
      </section>

      <section className="board-grid">
        {COLUMNS.map((column) => (
          <BoardColumn
            key={column.key}
            column={column}
            tasks={tasks.filter((task) => task.status === column.key)}
            onStatusChange={handleStatusChange}
          />
        ))}
      </section>
    </main>
  );
}