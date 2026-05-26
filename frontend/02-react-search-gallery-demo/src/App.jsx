import { startTransition, useDeferredValue, useEffect, useState } from 'react';

const DATASET = {
  ui: [
    { id: 1, name: 'Cinder Cards', tag: 'dashboard', note: 'Warm analytics layout with strong hierarchy.' },
    { id: 2, name: 'Tide Forms', tag: 'forms', note: 'Lightweight account settings surface.' },
    { id: 3, name: 'Muse Feed', tag: 'content', note: 'Editorial feed with staggered highlights.' },
  ],
  charts: [
    { id: 4, name: 'Signal Board', tag: 'analytics', note: 'Dense KPI panel with anomaly callouts.' },
    { id: 5, name: 'Orbit Trends', tag: 'reporting', note: 'Layered trend lines and cohort segments.' },
    { id: 6, name: 'Pulse Bars', tag: 'metrics', note: 'Compact comparisons for weekly snapshots.' },
  ],
  motion: [
    { id: 7, name: 'Ribbon Intro', tag: 'animation', note: 'Hero animation for page entry.' },
    { id: 8, name: 'Dock Reveal', tag: 'microinteraction', note: 'Bottom action rail with staged reveal.' },
    { id: 9, name: 'Scene Shift', tag: 'transition', note: 'Section transition with layered masks.' },
  ],
};

function GalleryCard({ item }) {
  return (
    <article className="gallery-card">
      <p className="chip">{item.tag}</p>
      <h3>{item.name}</h3>
      <p>{item.note}</p>
    </article>
  );
}

export default function App() {
  const [category, setCategory] = useState('ui');
  const [query, setQuery] = useState('');
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const deferredQuery = useDeferredValue(query);

  useEffect(() => {
    setLoading(true);
    const timer = window.setTimeout(() => {
      setItems(DATASET[category]);
      setLoading(false);
    }, 450);

    return () => window.clearTimeout(timer);
  }, [category]);

  const visibleItems = items.filter((item) => {
    const keyword = deferredQuery.trim().toLowerCase();
    if (!keyword) {
      return true;
    }
    return [item.name, item.tag, item.note].some((field) => field.toLowerCase().includes(keyword));
  });

  function handleCategoryChange(nextCategory) {
    startTransition(() => {
      setCategory(nextCategory);
      setQuery('');
    });
  }

  return (
    <main className="gallery-page">
      <section className="gallery-hero">
        <div>
          <p className="eyebrow">React Demo 02</p>
          <h1>Async search gallery with deferred filtering</h1>
          <p className="lead">
            Switch datasets, simulate network latency, and filter the current collection without freezing the input.
          </p>
        </div>

        <div className="control-panel">
          <div className="segment-row">
            {Object.keys(DATASET).map((key) => (
              <button
                key={key}
                type="button"
                className={key === category ? 'segment active' : 'segment'}
                onClick={() => handleCategoryChange(key)}
              >
                {key}
              </button>
            ))}
          </div>
          <label className="search-box">
            <span>Search current gallery</span>
            <input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Try analytics or animation" />
          </label>
        </div>
      </section>

      <section className="results-panel">
        {loading ? <p className="status-banner">Loading {category} references...</p> : null}
        {!loading && visibleItems.length === 0 ? <p className="status-banner">No matching references for this filter.</p> : null}
        <div className="gallery-grid">
          {!loading && visibleItems.map((item) => <GalleryCard key={item.id} item={item} />)}
        </div>
      </section>
    </main>
  );
}