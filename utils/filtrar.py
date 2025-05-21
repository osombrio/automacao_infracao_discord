from models.regra import Regra
def processar_comando(comando: str, regras: list):
    if comando.startswith("/filtrar_and "):
        argumentos = comando[len("/filtrar_and "):].strip()
        filtros = parse_filtros(argumentos)
        resultado = Regra.filtrar_regras(regras, **filtros)
        printar_regras(resultado)

    elif comando.startswith("/filtrar_or "):
        argumentos = comando[len("/filtrar_or "):].strip()
        filtros = parse_filtros(argumentos)
        resultado = Regra.filtrar_regras_qualquer(regras, **filtros)
        printar_regras(resultado)

def parse_filtros(argumentos: str) -> dict:
    filtros = {}
    for arg in argumentos.split():
        if '=' in arg:
            chave, valor = arg.split('=', 1)
            # Converte para tipo apropriado (bool, int, etc.)
            if valor.lower() == "true":
                valor = True
            elif valor.lower() == "false":
                valor = False
            elif valor.isdigit():
                valor = int(valor)
            filtros[chave] = valor
    return filtros

def printar_regras(regras):
    if not regras:
        print("Nenhuma regra encontrada com os filtros fornecidos.")
    for r in regras:
        print(r.gerar_template())
