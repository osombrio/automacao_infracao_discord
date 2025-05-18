def test_codigos_multiplos():
    from models.regra import Regra
    regra = Regra(cod="1,2,3", desc="Teste", punicao=3, identificador=200)
    contexto = {"cod": "2", "desc": "Teste", "prova": True, "intencao": True, "privado": False, "punicao": 3}
    assert regra.se_aplica(contexto) is True
