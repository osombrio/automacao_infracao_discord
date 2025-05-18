# tests/test_avalia_infracao.py
from models.regra import Regra
from models.avalia_infracao import avaliar_infracoes

def test_avaliar_infracoes_aplicavel():
    regra = Regra(
        categoria="Conduta",
        cod="1",
        desc="violencia",
        intencao=False,
        prova=True,
        punicao="5",
        reincidencia=False,
        prazo=False,
        cumulativa=False,
        condicao=None,
        exclusao=None,
        relacionadas=None,
        privado=False
    )

    contexto = {
        "cod": "1",
        "desc": "Ato de violência",
        "prova": True,
        "intencao": False,
        "reincidencia": False,
        "privado": False
    }

    resultado = avaliar_infracoes([regra], contexto)
    # assert resultado["pontuacao_total"] == 5
    assert resultado["regras_aplicadas"][0]["cod"] == "1"
