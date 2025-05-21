from models.avalia_infracao import avaliar_infracoes
from models.regra import Regra
from utils.filtrar import printar_regras
from utils.filtrar import parse_filtros
from utils.filtrar import processar_comando
from int_and_out.input_avaliacao import inputar_contexto
from utils.template import TEMPLATE
from utils.parse_format_int import parse_numeric_value

class MenuInterativo:
    def __init__(self, regras: list):
        self.regras = regras

    def exibir_opcoes(self):
        print("=== MENU ===")
        print("1. Exibir todas as regras")
        print("2. Filtrar regras (SOMENTE estes campos)")
        print("3. Filtrar regras (QUALQUER um dos campos)")
        print("4. Sair")
        print("5. Buscar regra por ID ou código")  # Novo
        print("6. Avaliar contexto de infração")   # Novo
        print("7. Ajuda")


    def iniciar(self):
        while True:
            self.exibir_opcoes()
            escolha = input("Escolha uma opção: ").strip()

            if escolha == "1":
                printar_regras(self.regras)

            elif escolha == "2":
                filtro = input("Digite os filtros (ex: categoria=Grave prova=True): ")
                filtros = parse_filtros(filtro)
                if not filtros:
                    print("[ERRO] Nenhum filtro válido foi informado.")
                    continue
                regras_filtradas = Regra.filtrar_regras(self.regras, **filtros)
                printar_regras(regras_filtradas)

            elif escolha == "3":
                filtro = input("Digite os filtros (ex: categoria=Leve desc=spam): ")
                filtros = parse_filtros(filtro)
                if not filtros:
                    print("[ERRO] Nenhum filtro válido foi informado.")
                    continue
                regras_filtradas = Regra.filtrar_regras_qualquer(self.regras, **filtros)
                printar_regras(regras_filtradas)

            elif escolha == "4":
                print("Saindo...")
                break
            
            
            # Dentro da função iniciar() do Menu:

            elif escolha == "6":
                contexto = inputar_contexto()
                resultados = avaliar_infracoes(self.regras, contexto)
                
                if not resultados:
                    print("Nenhuma infração aplicável encontrada para este contexto.")
                else:
                    print("\nInfrações aplicáveis encontradas:")
                    for regra in resultados:
                        # Seleciona o campo com base na reincidência do contexto
                        usar_reincidencia = contexto.get(TEMPLATE.reincidencia.nome, False)
                        raw = regra.reincidencia if usar_reincidencia else regra.punicao
                        pontuacao = parse_numeric_value(raw)
                
                        print(f"→ Regra ID {regra.identificador}")
                        print(f"   Descrição: {regra.desc}")
                        print(f"   Punição bruta: {raw}")
                        print(f"   Pontuação interpretada: {pontuacao if isinstance(pontuacao, (int, float)) else 'N/A'}\n")
            
            elif escolha == "7":
                exibir_ajuda()

            
            else:
                print("Opção inválida. Tente novamente.")


def exibir_ajuda():
    print("\n=== AJUDA ===")
    print("Este sistema é utilizado para consultar, filtrar e aplicar regras de moderação com base em contexto.")
    print("\n📘 COMO USAR:")
    print(" - As regras podem ser consultadas diretamente (opção 1), filtradas por critérios (opções 2 e 3), ou avaliadas com contexto (opção 6).")
    print("\n🧩 ESTRUTURA DAS REGRAS:")
    print("Cada regra possui os seguintes campos:")
    print(" - identificador: ID da regra")
    print(" - categoria: Leve, Média, Grave")
    print(" - cod: Códigos numéricos associados")
    print(" - desc: Descrição da infração")
    print(" - punicao: Punição padrão (ex: '3 pontos', 'Banimento')")
    print(" - reincidencia: Punição alternativa caso haja reincidência")
    print(" - cumulativa: Se pode ser somada a outras punições")
    print(" - prova, intencao, privado, prazo: Condições booleanas para aplicar a regra")
    print("\n⚖️ COMO FUNCIONA A AVALIAÇÃO DE INFRAÇÕES:")
    print(" - A função 'avaliar_infracoes' recebe o contexto (como prova=True, cod='11', etc.) e retorna as regras aplicáveis.")
    print(" - Se houver reincidência (contexto['reincidencia'] = True), é usada a punição definida no campo 'reincidencia'.")
    print(" - A regra principal é aquela com maior punição não cumulativa. Regras cumulativas são somadas à pontuação.")
    print("\n🔢 COMO SÃO CALCULADAS AS PUNIÇÕES:")
    print(" - O sistema tenta extrair valores numéricos dos campos 'punicao' e 'reincidencia'.")
    print("   Exemplos: '3 pontos' → 3 | 'Banimento' ou 'NA' → ignorado no cálculo.")
    print("\n🔍 FILTROS:")
    print(" - Use filtros no formato campo=valor, separados por espaço.")
    print("   Exemplo: categoria=Grave prova=True")
    print(" - Opção 2 (filtrar todos os campos): aplica o filtro estritamente (todos os campos devem bater).")
    print(" - Opção 3 (filtrar qualquer campo): considera uma regra se ao menos UM campo for compatível.")
    print("\nℹ️ DICAS:")
    print(" - Certifique-se de digitar os nomes dos campos corretamente nos filtros.")
    print(" - Valores booleanos devem ser True ou False.")
    print(" - Use o comando 6 para simular a aplicação de regras a um determinado contexto.")
    print("\n============================\n")
