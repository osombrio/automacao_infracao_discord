import unicodedata

def normalizar_nome(nome: str) -> str:
    text = unicodedata.normalize("NFKD", nome)
    text = text.encode("ASCII", "ignore").decode("utf-8")
    return text.strip().lower().replace(" ", "_")
