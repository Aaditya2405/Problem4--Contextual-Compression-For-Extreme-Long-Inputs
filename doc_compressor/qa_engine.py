import re

STOPWORDS = {
    "the", "is", "are", "was", "were", "be", "been", "being",
    "of", "to", "and", "or", "in", "on", "for", "with", "about",
    "what", "does", "say", "this", "that", "it", "as", "by"
}

def tokenize(text):
    return [
        w for w in re.findall(r"\w+", text.lower())
        if w not in STOPWORDS
    ]

def score_chunk(chunk_text, question):
    q_words = set(tokenize(question))
    c_words = set(tokenize(chunk_text))
    return len(q_words & c_words)

def answer_question(question, summaries):
    best_score = 0
    best_idx = None
    best_summary = None

    for idx, summary in enumerate(summaries):
        score = score_chunk(summary, question)
        if score > best_score:
            best_score = score
            best_summary = summary
            best_idx = idx

    if best_summary:
        return {
            "answer": best_summary,
            "why": f"Matched {best_score} key terms from the question",
            "source_chunk": best_idx + 1,
            "confidence": round(min(0.3 + best_score * 0.15, 0.9), 2)
        }

    return {
        "answer": "Answer not found in the document.",
        "why": "No relevant keyword match",
        "source_chunk": None,
        "confidence": 0.0
    }
