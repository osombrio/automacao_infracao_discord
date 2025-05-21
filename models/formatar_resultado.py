from utils.parse_format_int import parse_numeric_value
from utils.template import TEMPLATE


# def formatar_resultado(regras: list, contexto: dict) -> str:
def formatar_resultado(regras: list, contexto: dict) -> str:
    total = 0
    resultado = []

    for r in regras:
        # Usa campo correto conforme o contexto de reincidência
        raw_value = r.reincidencia if contexto.get("reincidencia") else r.punicao
        # print(f"[DEBUG - formatar_resultado] Regra {r.identificador}: valor bruto = {raw_value}")

        pts = parse_numeric_value(raw_value)

        if isinstance(pts, (int, float)) and pts > 0:
            total += pts
            resultado.append(f"→ Pontuação da regra {r.identificador}: {pts}")
        elif isinstance(pts, (int, float)) and pts == 0:
            # Evita mostrar regras com 0 pontos
            continue
        else:
            # Caso como "Banimento", "NA", etc.
            resultado.append(f"→ Regra {r.identificador}: punição = {raw_value}")

    regras_texto = "\n".join(r.gerar_template() for r in regras)
    pontuacoes_texto = "\n".join(resultado)

    return f"{regras_texto}\n{pontuacoes_texto}\nPunição Final: {total} ponto(s)"

