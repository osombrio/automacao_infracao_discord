def test_pontuacao_simples():
    from models.regra import Regra

    regra = Regra(cod="1", desc="Teste", punicao=2, prazo=False, identificador=100)
    contexto = {
        "cod": "1",
        "desc": "Teste",
        "prova": True,
        "intencao": True,
        "privado": False,
        "reincidencia": 3,
        "punicao": 2
    }

    assert regra.se_aplica(contexto) is True
    assert regra.retornar_pontuacao(contexto) == 2
