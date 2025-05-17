from utils.template import TEMPLATE

def validar_contexto(contexto: dict) -> dict:
    obrigatorios = [TEMPLATE.cod.nome]  # Removido "descricao"
    for campo in obrigatorios:
        if campo not in contexto:
            raise ValueError(f"Falta campo '{campo}'.")
    # Tipagem mínima, se desejar pode reforçar com isinstance()
    return contexto
