def test_regra_com_prova_obrigatoria():
    from models.regra import Regra
    regra = Regra(cod="10", desc="Prova obrigatória", prova=True, punicao=2, identificador=202)
    contexto = {"cod": "10", "desc": "Teste", "prova": False, "intencao": True, "privado": False, "punicao": 2}
    assert regra.se_aplica(contexto) is False
