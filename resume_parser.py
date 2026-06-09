def extract_text(file_content):
    try:
        return file_content.decode("utf-8", errors="ignore")
    except:
        return str(file_content)
