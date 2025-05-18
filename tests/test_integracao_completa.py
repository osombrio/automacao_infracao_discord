def test_fluxo_inteiro():
    from models.regra import Regra
    from main import avaliar_infracoes

    regras = [
        Regra(cod="1", desc="Teste A", punicao=2, identificador=301),
        Regra(cod="2", desc="Teste B", prova=True, punicao=3, identificador=302),
    ]
    contexto = {
        "cod": "1,2",
        "desc": "Teste A",
        "prova": True,
        "intencao": True,
        "privado": False,
        "reincidencia": False,
        "punicao": 2,
    }

    aplicaveis = avaliar_infracoes(regras, contexto)
    assert len(aplicaveis) == 2
    assert any(r.cod == "1" for r in aplicaveis)
    assert any(r.cod == "2" for r in aplicaveis)
