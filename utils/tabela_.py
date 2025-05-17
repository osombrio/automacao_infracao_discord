from typing import List
from utils.normalizador import normalizar_nome   # Usa o módulo criado
from utils.template import TEMPLATE
# utils/tabela_.py

from utils.estrutura_coluna import Coluna
from utils.template import TEMPLATE

class Grade:
    def __init__(self, row, colunas):
        self.row = row
        self.colunas = colunas

class Bloco:
    def __init__(self, valor, nome_campo):
        self.valor = valor
        self.nome_campo = nome_campo

class Linha:
    def __init__(self, **kwargs):
        for chave, bloco in kwargs.items():
            if not isinstance(bloco, Bloco):
                raise TypeError(f"Esperado Bloco em '{chave}', mas recebeu {type(bloco).__name__}")
            setattr(self, chave, bloco)

class _TabelaPlanilha:
    def requestLinha(self, row, colunas):
        def get_bloco(attr: str) -> Bloco:
            coluna_template = getattr(TEMPLATE, attr)
            idx = colunas[normalizar_nome(coluna_template.ID)]
            return Bloco(row[idx], attr)

        dados_linha = {
            attr: get_bloco(attr)
            for attr in vars(TEMPLATE)
            if isinstance(getattr(TEMPLATE, attr), Coluna)
        }

        return Linha(**dados_linha)

