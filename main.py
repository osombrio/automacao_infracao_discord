
from models.avalia_infracao import avaliar_infracoes
from models.contexto import validar_contexto
from models.criar_dados import criar_regra_do_usuario
from utils.leitor_excel import carregar_regras
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def testar_com_varios_contextos(arq_regras, contextos):
    print("Carregando regras...")
    try:
        regras = carregar_regras(arq_regras)
    except (ValueError, TypeError) as e:
        print("Erro ao carregar o arquivo de regras:", e)
        return

    for i, contexto in enumerate(contextos, 1):
        print(f"\n=== Teste {i} ===")
        try:
            contexto_validado = validar_contexto(contexto)
        except (ValueError, TypeError) as e:
            print("Erro na validação do contexto:", e)
            continue

        infracao = criar_regra_do_usuario(contexto_validado)

        resultado = avaliar_infracoes(regras, infracao)
        print("Contexto:", contexto)
        print("Resultado da avaliação:")
        print(resultado)

def main():
    print("Gerenciador de Punições - Testes múltiplos (v1.0)")

    arq = "data/infracoes.xlsx"
    contextos = []
    contextos.append(
        {
            "cod": "12",
            "desc": "Teste hipotetico",
            "prova": True,
            "intencao": True,
            "privado": False,
            "reincidencia": False
        }
    )
    '''
    contextos = [
        {
            "cod": "1,2",
            "desc": "Z",
            "prova": True,
            "intencao": False,
            "privado": False,
            "reincidencia": False
        },
        {
            "cod": "3,5",
            "desc": "Y",
            "prova": False,
            "intencao": True,
            "privado": True,
            "reincidencia": True
        },
        {
            "cod": "4",
            "desc": "X",
            "prova": False,
            "intencao": True,
            "privado": False,
            "reincidencia": False
        }
        # Pode adicionar quantos contextos quiser
    ]
    '''
    testar_com_varios_contextos(arq, contextos)

if __name__ == "__main__":
    main()
