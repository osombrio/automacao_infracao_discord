from models.criar_dados import criar_regra_do_usuario
from models.regra import Regra

def test_criar_regra_do_usuario_basico():
    contexto = {
        "cod": "1,2",
        "desc": "Usou linguagem imprópria",
        "prova": True,
        "intencao": False,
        "privado": False,
        "reincidencia": False
    }

    regra = criar_regra_do_usuario(contexto)

    assert isinstance(regra, Regra)
    assert regra.cod == "1,2"
    assert regra.desc == "Usou linguagem imprópria"
    assert regra.prova is True
    assert regra.intencao is False
    assert regra.privado is False
    assert regra.reincidencia is False
