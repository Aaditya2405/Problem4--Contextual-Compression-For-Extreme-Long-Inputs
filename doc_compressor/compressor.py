def compress_chunks(chunks):
    compressed = {
        "section_summaries": [],
        "key_facts": [],
        "risks": [],
        "exceptions": []
    }

    for idx, chunk in enumerate(chunks):
        text = chunk.lower()

        # smarter rule-based summary
        if "risk" in text:
            summary = "This section discusses risk management and related safeguards."
        elif "security" in text:
            summary = "This section discusses security and protection measures."
        elif "personal data" in text:
            summary = "This section discusses processing of personal data."
        else:
            summary = chunk.split(".")[0].strip() + "."

        compressed["section_summaries"].append({
            "chunk_id": idx + 1,
            "summary": summary
        })

    return compressed
