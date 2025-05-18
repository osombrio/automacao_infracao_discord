def test_pontuacao_invalida():
    from models.regra import Regra

    regra = Regra(cod="3", desc="Inválida", punicao="abc", identificador=102)
    contexto = {
        "cod": "3",
        "desc": "Inválida",
        "prova": True,
        "intencao": True,
        "privado": False,
        "punicao": "abc"
    }

    assert regra.se_aplica(contexto) is True
    assert regra.retornar_pontuacao(contexto) == 0  # Valor inválido deve virar 0
