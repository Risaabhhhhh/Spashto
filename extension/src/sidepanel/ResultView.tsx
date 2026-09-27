import React, { useEffect, useState } from 'react';
import { simplify, submitFeedback } from '../lib/api-client';
import { storage } from '../lib/storage';

interface Props {
  targetLang: string;
}

const ResultView: React.FC<Props> = ({ targetLang }) => {
  const [originalText, setOriginalText] = useState<string>('');
  const [simplifiedText, setSimplifiedText] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const [feedbackSent, setFeedbackSent] = useState<boolean>(false);

  const processSimplification = async (text: string) => {
    if (!text) return;
    setOriginalText(text);
    setLoading(true);
    setError('');
    setSimplifiedText('');
    setFeedbackSent(false);

    try {
      const res = await simplify(text, targetLang);
      setSimplifiedText(res.simplified_text);
    } catch (err: any) {
      setError(err.message || "An unknown error occurred.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    storage.get('spashto_selected_text').then(text => {
      if (text) processSimplification(text);
    });

    storage.listen('spashto_selected_text', (newText) => {
      if (newText) processSimplification(newText);
    });
  }, [targetLang]); // re-run if language changes and we have text

  const handleFeedback = async (type: string) => {
    try {
      await submitFeedback(originalText, simplifiedText, type);
      setFeedbackSent(true);
    } catch (err) {
      console.error(err);
    }
  };

  if (!originalText && !loading && !error) {
    return (
      <div style={{ color: '#666', fontSize: '14px', padding: '12px', backgroundColor: '#f0f0f0', borderRadius: '6px' }}>
        Select some legal/government text on a webpage, right-click, and choose <strong>"Simplify this"</strong>.
      </div>
    );
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
      <div>
        <h3 style={{ fontSize: '14px', color: '#666', margin: '0 0 4px 0' }}>Original Text:</h3>
        <div style={{ fontSize: '14px', backgroundColor: '#eaeaea', padding: '10px', borderRadius: '6px', color: '#444', fontStyle: 'italic', maxHeight: '100px', overflowY: 'auto' }}>
          {originalText}
        </div>
      </div>

      <div>
        <h3 style={{ fontSize: '14px', color: '#666', margin: '0 0 4px 0' }}>Simplified Result:</h3>
        {loading ? (
          <div style={{ fontSize: '14px', color: '#0066cc', padding: '10px', backgroundColor: '#e6f2ff', borderRadius: '6px' }}>
            Simplifying text... Please wait.
          </div>
        ) : error ? (
          <div style={{ fontSize: '14px', color: '#cc0000', padding: '10px', backgroundColor: '#ffe6e6', borderRadius: '6px' }}>
            {error}
          </div>
        ) : simplifiedText ? (
          <div style={{ fontSize: '14px', backgroundColor: '#e6ffe6', padding: '10px', borderRadius: '6px', color: '#004d00' }}>
            {simplifiedText}
            {!feedbackSent ? (
              <div style={{ marginTop: '12px', display: 'flex', gap: '8px' }}>
                <span style={{ fontSize: '12px', color: '#555', alignSelf: 'center' }}>Was this helpful?</span>
                <button onClick={() => handleFeedback('positive')} style={{ padding: '4px 8px', cursor: 'pointer' }}>👍 Yes</button>
                <button onClick={() => handleFeedback('negative')} style={{ padding: '4px 8px', cursor: 'pointer' }}>👎 No</button>
              </div>
            ) : (
              <div style={{ marginTop: '12px', fontSize: '12px', color: '#555' }}>Thank you for your feedback!</div>
            )}
          </div>
        ) : null}
      </div>
    </div>
  );
};

export default ResultView;
