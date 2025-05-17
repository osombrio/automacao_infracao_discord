# utils/template.py

from utils.estrutura_coluna import Coluna

class TEMPLATE:
   
   categoria = Coluna("categoria", "Categoria", "")
   cod = Coluna("cod", "Regras", "")
   desc = Coluna("desc", "Infração", "")
   intencao = Coluna("intencao", "Sem Intencionalidade", True)
   prova = Coluna("prova", "Prova detalhada", False)
   punicao = Coluna("punicao", "Punição pontos", "")
   reincidencia = Coluna("reincidencia", "Reincidencia", "")
   prazo = Coluna("prazo", "Prazo punição", False)
   cumulativa = Coluna("cumulativa", "Cumulativa", False)
   condicao = Coluna("condicao", "Condição", "")
   exclusao = Coluna("exclusao", "Exclusão", "")
   relacionadas = Coluna("relacionadas", "Relacionada", "")
   privado = Coluna("privado", "Contexto privado", False)
   identificador = Coluna("identificador", "ID Infração", -1)

