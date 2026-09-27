import React, { useState } from 'react';
import { guideQuery } from '../lib/api-client';

interface Props {
  lang: string;
}

const QueryBox: React.FC<Props> = ({ lang }) => {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [results, setResults] = useState<{chunks: string[], sources: string[]} | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;
    
    setLoading(true);
    setError('');
    setResults(null);
    
    try {
      const res = await guideQuery(query, lang);
      setResults({ chunks: res.answer_chunks, sources: res.sources });
    } catch (err: any) {
      setError(err.message || "Failed to retrieve tax guide information.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '8px' }}>
        <input 
          type="text" 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
          placeholder="Ask a tax procedural question..."
          style={{ flex: 1, padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
        />
        <button type="submit" disabled={loading || !query.trim()} style={{ padding: '8px 12px', cursor: 'pointer' }}>
          Search
        </button>
      </form>

      {loading && (
        <div style={{ fontSize: '14px', color: '#0066cc' }}>Searching tax guidelines...</div>
      )}

      {error && (
        <div style={{ fontSize: '14px', color: '#cc0000', padding: '10px', backgroundColor: '#ffe6e6', borderRadius: '6px' }}>
          {error}
        </div>
      )}

      {results && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {results.chunks.length > 0 ? (
            results.chunks.map((chunk, idx) => (
              <div key={idx} style={{ fontSize: '14px', padding: '10px', backgroundColor: '#fff', border: '1px solid #ddd', borderRadius: '6px' }}>
                {chunk}
              </div>
            ))
          ) : (
            <div style={{ fontSize: '14px', color: '#666' }}>No relevant tax guidance found.</div>
          )}
          
          {results.sources.length > 0 && (
            <div>
              <strong style={{ fontSize: '12px', color: '#555' }}>Sources:</strong>
              <ul style={{ margin: '4px 0 0 0', paddingLeft: '20px', fontSize: '12px' }}>
                {results.sources.map((src, idx) => (
                  <li key={idx}><a href={src} target="_blank" rel="noopener noreferrer">{src}</a></li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default QueryBox;
