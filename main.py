from models.formatar_resultado import formatar_resultado
from models.avalia_infracao import avaliar_infracoes
from models.contexto import validar_contexto
from models.criar_dados import criar_regra_do_usuario
from models.regra import Regra
from utils.interpreta_comando import interpretar_comando_punir
from utils.leitor_excel import carregar_regras
import sys
import os
from utils.filtrar import processar_comando
from utils.filtrar import parse_filtros
from utils.filtrar import printar_regras
from int_and_out.menu import MenuInterativo

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
        regras_aplicaveis = avaliar_infracoes(regras, infracao)
        resultado = formatar_resultado(regras_aplicaveis, contexto_validado)
        print("Contexto:", contexto)
        print("Resultado da avaliação:")
        print(resultado)

def main():
    print("Gerenciador de Punições - Testes múltiplos (v1.0)")

    arq = "data/infracoes.xlsx"

    contextos = list()
    contextos.append(interpretar_comando_punir(
        "/punir cod:11 prova:True intencao:True privado:False reincidencia:True"))
    '''
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
    # testar_com_varios_contextos(arq, contextos)

    # Suponha que `regras` seja uma lista de instâncias da classe `Regra`
    
    regras = carregar_regras(arq)
    # Buscar todas as regras com categoria "Grave" e punição contendo "Banimento"
    '''
    regras_filtradas = Regra.filtrar_regras_qualquer(regras, categoria="Grave", punicao="Banimento")

    comando = "/filtrar_or categoria=Leve desc=spam"
    
    processar_comando(comando, regras)
    
    # Mostrar resultado
    for r in regras_filtradas:
        print(r.gerar_template())
    
    '''
    
    menu = MenuInterativo(regras)
    menu.iniciar()





if __name__ == "__main__":
    main()
