from utils.parse_format_int import parse_numeric_value

def formatar_resultado(regras: list, contexto: dict) -> str:
    total = 0
    for r in regras:
        pts = parse_numeric_value(r.retornar_pontuacao(contexto))
        if isinstance(pts, (int, float)):
            print(f"→ Pontuação da regra {r.identificador}: {pts}")
            total += pts

    txt = "\n".join(r.gerar_template() for r in regras)
    return f"{txt}\nPunição Final: {total} ponto(s)"
