import re

def clean_text(text: str) -> str:
    """
    Cleans raw extracted text by:
    - removing extra newlines
    - normalizing spaces
    - trimming whitespace
    """

    if not text or text.strip() == "":
        return ""

    # Convert multiple newlines to max two (paragraph separation)
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    # Replace multiple spaces/tabs with single space
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text
