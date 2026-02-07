from pypdf import PdfReader
import os

def extract_text_from_pdf(path):
    reader = PdfReader(path)

    print("Pages found:", len(reader.pages))  # DEBUG

    text = ""
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        print(f"Page {i} text length:", 0 if page_text is None else len(page_text))

        if page_text:
            text += page_text + "\n"

    return text
