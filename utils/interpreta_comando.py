import re

from utils.template import TEMPLATE


def retornar_comando(comando: str):
    return re.findall(r'(\w+):("[^"]+"|\S+)', comando)

def interpretar_comando_punir(comando: str) -> dict:
    if not comando.startswith("/punir"):
        raise ValueError("Comando inválido: deve começar com /punir")

    # Regex para capturar chave:valor (com ou sem aspas)
    padrao = retornar_comando(comando)

    contexto = {}
    for chave, valor in padrao:
        valor = valor.strip('"')
        if valor.lower() in ("true", "false"):
            contexto[chave] = valor.lower() == "true"
        else:
            contexto[chave] = valor

    # Validação mínima
    if TEMPLATE.cod.nome not in contexto and TEMPLATE.identificador.nome not in contexto:
        raise ValueError("Comando deve conter pelo menos 'TEMPLATE.cod.nome' ou 'TEMPLATE.identificador.nome'.")

    return contexto
