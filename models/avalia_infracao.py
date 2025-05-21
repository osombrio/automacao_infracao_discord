from utils import parse_format_int
from utils.parse_format_int import parse_numeric_value
from utils.template import TEMPLATE
from models.regra import Regra

def avaliar_infracoes(regras: list, contexto: dict) -> list:
    aplicaveis = [r for r in regras if r.se_aplica(contexto)]
    if not aplicaveis:
        return []

    cumul = [r for r in aplicaveis if r.cumulativa]
    naoc = [r for r in aplicaveis if not r.cumulativa]
    principal = max(naoc, key=lambda r: r.punicao or 0, default=None)
    total = 0
    usados = []

    def obter_pontuacao(regra):
        raw = regra.reincidencia if Regra.obter_valor(contexto, TEMPLATE.reincidencia.nome) else regra.punicao
        return parse_numeric_value(raw)

    if principal:
        pts = obter_pontuacao(principal)
        # print(f"Regra {principal.identificador} - pontuação: {pts} - punição bruta: {principal.punicao}")
        if isinstance(pts, (int, float)):
            total += pts
        usados.append(principal)

    for r in cumul:
        if not principal or r.punicao:
            pts = obter_pontuacao(r)
            # print(f"Regra {r.identificador} - pontuação: {pts} - punição bruta: {r.punicao}")
            if isinstance(pts, (int, float)):
                total += pts
            usados.append(r)

    return usados
