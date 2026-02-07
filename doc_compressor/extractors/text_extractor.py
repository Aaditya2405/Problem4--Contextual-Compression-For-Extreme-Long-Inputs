def extract_text_from_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
        print("TXT LENGTH:", len(data))   # DEBUG
        return data
