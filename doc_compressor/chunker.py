def chunk_text(text, chunk_size=500, overlap=50):
    """
    Splits cleaned text into overlapping chunks.

    Args:
        text (str): Cleaned input text
        chunk_size (int): Max characters per chunk
        overlap (int): Overlap between chunks

    Returns:
        list[str]: List of text chunks
    """

    if not text or text.strip() == "":
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]

        chunk = chunk.strip()
        if len(chunk) > 50:   # avoid tiny tail chunks
            chunks.append(chunk)


        start = end - overlap
        if start < 0:
            start = 0

    return chunks
