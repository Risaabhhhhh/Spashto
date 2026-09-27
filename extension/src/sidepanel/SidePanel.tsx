import React, { useState } from 'react';
import QueryBox from './QueryBox';
import ResultView from './ResultView';

const SidePanel: React.FC = () => {
  const [targetLang, setTargetLang] = useState<string>("en");

  return (
    <div style={{ padding: '16px', display: 'flex', flexDirection: 'column', gap: '24px' }}>
      <header style={{ borderBottom: '1px solid #ddd', paddingBottom: '12px' }}>
        <h1 style={{ fontSize: '20px', margin: '0 0 8px 0', color: '#333' }}>Spashto</h1>
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
          <label style={{ fontSize: '14px', color: '#555' }}>Language:</label>
          <select 
            value={targetLang} 
            onChange={(e) => setTargetLang(e.target.value)}
            style={{ padding: '4px', borderRadius: '4px', border: '1px solid #ccc' }}
          >
            <option value="en">English</option>
            <option value="hi">Hindi</option>
          </select>
        </div>
      </header>
      
      <section>
        <ResultView targetLang={targetLang} />
      </section>
      
      <section style={{ borderTop: '1px solid #ddd', paddingTop: '16px' }}>
        <h2 style={{ fontSize: '16px', margin: '0 0 12px 0', color: '#444' }}>Tax Guide</h2>
        <QueryBox lang={targetLang} />
      </section>
    </div>
  );
};

export default SidePanel;
