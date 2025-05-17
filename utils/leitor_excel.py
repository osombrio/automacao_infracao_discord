from utils.estrutura_coluna import Coluna  # ou from utils.tabela_ import Coluna (se não separou)
from utils.tabela_ import _TabelaPlanilha
from utils.template import TEMPLATE
from models.regra import Regra
from utils.normalizador import normalizar_nome  # se estiver separada a função

import openpyxl

import unicodedata

def normalizar_nome(nome: str) -> str:
    nome = unicodedata.normalize("NFKD", nome)
    nome = nome.encode("ASCII", "ignore").decode("utf-8")
    nome = nome.strip().lower().replace(" ", "_")
    return nome


def carregar_regras(path_planilha: str) -> list[Regra]:
    wb = openpyxl.load_workbook(path_planilha, data_only=True)
    sheet = wb.active

    cabecalho = [normalizar_nome(str(cell.value)) for cell in sheet[1]]
    colunas = {nome: idx for idx, nome in enumerate(cabecalho)}

    tabela = _TabelaPlanilha()
    linhas = [
        tabela.requestLinha(row, colunas)
        for row in sheet.iter_rows(min_row=2, values_only=True)
        if not all(cell is None for cell in row)
    ]

    # Converte Linhas → Regras
    regras = []
    for linha in linhas:
        r = Regra.__new__(Regra)
        for coluna in vars(TEMPLATE).values():
            if isinstance(coluna, Coluna):
                nome = coluna.nome  # nome lógico usado como atributo em `Linha`
                bloco = getattr(linha, nome, None)
                valor = bloco.valor if bloco else None
                setattr(r, nome, valor)
        regras.append(r)

    return regras
