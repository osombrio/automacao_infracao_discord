def test_pontuacao_com_prazo():
    from models.regra import Regra

    regra = Regra(cod="2", desc="Com Prazo", prazo=True, reincidencia=5, identificador=101)
    contexto = {
        "cod": "2",
        "desc": "Com Prazo",
        "prova": True,
        "intencao": True,
        "privado": False,
        "reincidencia": 5,
        "punicao": 1
    }

    assert regra.se_aplica(contexto) is True
    assert regra.retornar_pontuacao(contexto) == 5
