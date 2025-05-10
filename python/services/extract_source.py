from urllib.parse import urlparse

def extract_source(url: str) -> str:
    return urlparse(url).netloc
