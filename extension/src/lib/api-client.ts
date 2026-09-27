const BASE_URL = "http://localhost:8000";

export async function simplify(text: string, targetLang: string = "en") {
  const res = await fetch(`${BASE_URL}/simplify`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, target_lang: targetLang })
  });
  if (!res.ok) throw new Error("Backend API failed during simplification");
  return res.json();
}

export async function guideQuery(query: string, lang: string = "en") {
  const res = await fetch(`${BASE_URL}/guide/query`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query, lang })
  });
  if (!res.ok) throw new Error("Backend API failed during tax query");
  return res.json();
}

export async function submitFeedback(text: string, simplifiedText: string, feedbackType: string) {
  const res = await fetch(`${BASE_URL}/feedback`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, simplified_text: simplifiedText, feedback_type: feedbackType })
  });
  if (!res.ok) throw new Error("Failed to submit feedback");
  return res.json();
}
