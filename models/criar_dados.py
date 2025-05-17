from models.contexto import validar_contexto
from models.regra import Regra
from utils.template import TEMPLATE
from utils.estrutura_coluna import Coluna

def criar_regra_do_usuario(contexto: dict) -> Regra:
    validar_contexto(contexto)

    args_regra = {}
    for attr in vars(TEMPLATE):
        coluna = getattr(TEMPLATE, attr)
        if isinstance(coluna, Coluna):
            valor = contexto.get(attr, None)
            args_regra[attr] = valor

    return Regra(**args_regra)
