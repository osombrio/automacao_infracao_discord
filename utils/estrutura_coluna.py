# utils/tabela_.py
class Coluna:
    def __init__(self, nome_logico, nome_excel, nome_init):
        self.nome = nome_logico
        self.ID = nome_excel
        self.nome_init = nome_init

    def __repr__(self):
        return f"<Coluna {self.nome} -> '{self.ID}'>"
