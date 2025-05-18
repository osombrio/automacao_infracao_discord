def test_regra_nao_aplicavel():
    from models.regra import Regra
    regra = Regra(cod="99", desc="Inexistente", punicao=1, identificador=201)
    contexto = {"cod": "1", "desc": "Outra coisa", "prova": True, "intencao": True, "privado": False, "punicao": 1}
    assert regra.se_aplica(contexto) is False
