from utils.parse_format_int import parse_numeric_value

def avaliar_infracoes(regras: list, contexto: dict) -> str:
    aplicaveis = [r for r in regras if r.se_aplica(contexto)]
    if not aplicaveis:
        return "Nenhuma infração aplicável."
    cumul = [r for r in aplicaveis if r.cumulativa]
    naoc = [r for r in aplicaveis if not r.cumulativa]
    principal = max(naoc, key=lambda r: r.punicao or 0, default=None)

    total = 0
    usados = []
    if principal:
        pts = parse_numeric_value(principal.retornar_pontuacao(contexto))
        if isinstance(pts, (int, float)):
            total += pts
        usados.append(principal)
    for r in cumul:
        # if not principal or (r.punicao or 0) >= (principal.punicao or 0):
        if not principal or (r.punicao or 0):
            pts = parse_numeric_value(r.retornar_pontuacao(contexto))
            if isinstance(pts, (int, float)):
                # print("A regra ", r.identificador, " somou acao: ", pts)
                total += pts
            usados.append(r)
    txt = "\n".join(r.gerar_template() for r in usados)
    return f"{txt}\nPunição Final: {total} ponto(s)"
