from utils import parse_format_int
from utils.parse_format_int import parse_numeric_value


def avaliar_infracoes(regras: list, contexto: dict) -> list:
    aplicaveis = [r for r in regras if r.se_aplica(contexto)]
    if not aplicaveis:
        return []

    cumul = [r for r in aplicaveis if r.cumulativa]
    naoc = [r for r in aplicaveis if not r.cumulativa]
    principal = max(naoc, key=lambda r: r.punicao or 0, default=None)

    usados = []
    if principal:
        usados.append(principal)
    usados.extend(c for c in cumul if c not in usados)

    for r in usados:
        pts = parse_numeric_value(r.retornar_pontuacao(contexto))
    print(f"Regra {r.identificador} - pontuação: {pts} - punicao bruta: {r.punicao}")


    return usados
