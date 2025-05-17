
from int_and_out import InterfaceUsuario
from utils import tabela_
'''
class dados_usuario:
    def __init__(self, contexto: dict, interface: InterfaceUsuario):
        self.contexto = contexto
        self.interface = interface

    def getByContexto(self, contexto):
        return self.get(contexto.ID,contexto.nome_init)

    def get(self, chave: str, padrao=None):
        """
        Tenta obter o valor da chave do contexto ou da interface.
        """

        if chave in self.contexto:
            return self.contexto[chave]
        return self.interface.solicitar_valor(chave) or padrao

'''