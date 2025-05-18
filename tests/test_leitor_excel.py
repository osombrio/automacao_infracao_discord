# tests/test_leitor_excel.py
import pytest
from utils.leitor_excel import carregar_regras
from models.regra import Regra
import os
path = os.path.join(os.path.dirname(__file__), "data/infracoes.xlsx")

def test_carregar_regras_com_arquivo_valido():
    # path = "data/infracoes_teste.xlsx"  # Use uma planilha de teste pequena e controlada
    regras = carregar_regras(path)
    assert isinstance(regras, list)
    assert all(isinstance(r, Regra) for r in regras)
    assert len(regras) > 0

def test_carregar_regras_com_arquivo_invalido():
    with pytest.raises(FileNotFoundError):
        carregar_regras("arquivo_inexistente.xlsx")
