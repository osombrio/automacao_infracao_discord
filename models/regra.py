from dataclasses import dataclass
from typing import Optional, Union

from utils.template import TEMPLATE


@dataclass
class Regra:
    identificador: Optional[int] = None
    categoria: Optional[str] = None
    cod: Optional[str] = None
    desc: Optional[str] = None
    intencao: Optional[bool] = None
    prova: Optional[bool] = None
    punicao: Optional[Union[int, str]] = None
    reincidencia: Optional[Union[int, str]] = None
    prazo: Optional[bool] = None
    cumulativa: Optional[bool] = None
    condicao: Optional[str] = None
    exclusao: Optional[str] = None
    relacionadas: Optional[str] = None
    privado: Optional[bool] = None


    def gerar_template(self):
        cod = self.cod or "Sem código"
        desc = self.desc or "Sem descrição"
        # return f"< ID {self.identificador} | Regra {cod} | Desc: {desc}>"
        return self.__str__()

    @staticmethod
    def obter_valor(origem, chave: str, default=None):
        if isinstance(origem, dict):
            return origem.get(chave, default)
        return getattr(origem, chave, default)

    @staticmethod
    def filtrar_regras_qualquer(regras: list, **filtros):
        resultado = []
        for regra in regras:
            correspondencias = []
            for campo, valor in filtros.items():
                campo_valor = Regra.obter_valor(regra, campo)
                if campo_valor is None:
                    continue
                if isinstance(campo_valor, str):
                    if str(valor).lower() in campo_valor.lower():
                        correspondencias.append(f"{campo}='{campo_valor}'")
                elif campo_valor == valor:
                    correspondencias.append(f"{campo}={campo_valor}")
            if correspondencias:
                # print(f"[DEBUG - filtro qualquer] Regra {regra.identificador} bateu com: {', '.join(correspondencias)}")
                resultado.append(regra)
        return resultado



    @staticmethod
    def filtrar_regras(regras: list, **filtros):
        resultado = []
        for regra in regras:
            match = True
            for campo, valor in filtros.items():
                campo_valor = Regra.obter_valor(regra, campo)
                if campo_valor is None:
                    match = False
                    break
                if isinstance(campo_valor, str):
                    if str(valor).lower() not in campo_valor.lower():
                        match = False
                        break
                elif campo_valor != valor:
                    match = False
                    break
            if match:
                # print(f"[DEBUG - filtro] Regra {regra.identificador} corresponde ao filtro: {filtros}")
                resultado.append(regra)
        return resultado

    @staticmethod
    def obter_todos(obj, prefixo):
        if isinstance(obj, dict):
            return {k: v for k, v in obj.items() if k.startswith(prefixo)}
        return {
            attr: getattr(obj, attr)
            for attr in dir(obj)
            if attr.startswith(prefixo) and not attr.startswith("__")
        }

    def se_aplica(self, contexto) -> bool:
        # Função auxiliar para pegar atributo de dict ou objeto
        '''
        def obter_valor(obj, chave, default=None):
            if isinstance(obj, dict):
                return obj.get(chave, default)
            return getattr(obj, chave, default)
        '''
        # print(f"\nAvaliar regra: {self}")
    
        codigos_contexto = self.obter_valor(contexto, TEMPLATE.cod.nome, "")
        # print(f"Códigos no contexto: {codigos_contexto}")
    
        if isinstance(codigos_contexto, str):
            codigos_contexto = [c.strip() for c in codigos_contexto.split(",")]
        elif not isinstance(codigos_contexto, list):
            codigos_contexto = [str(codigos_contexto)]

        cod = self.cod
        # print(f"Códigos da regra: {cod}")
    
        if isinstance(cod, str):
            cod = [c.strip() for c in cod.split(",")]
        elif not isinstance(cod, list):
            cod = [str(cod)]
    
        # Verifica se algum código da regra está no contexto
        if not any(c in codigos_contexto for c in cod):
            # print("-> Código da regra não corresponde ao contexto. Regra não se aplica.")
            return False
    
        # Pega a descrição (sem filtro condicao/exclusao)
        desc = (self.obter_valor(contexto, TEMPLATE.desc.nome, "") or "").lower()
        # print(f"Descrição no contexto: '{desc}'")
    
        if self.prova and not self.obter_valor(contexto, TEMPLATE.prova.nome, False):
            print("-> Prova detalhada exigida, mas contexto não tem prova. Regra não se aplica.")
            return False
    
        if not self.intencao and not self.obter_valor(contexto, TEMPLATE.intencao.nome, False):
            print("-> Regra permite punir sem intenção, mas contexto indica ausência de intenção. Regra não se aplica.")
            return False
    
        if not self.privado and self.obter_valor(contexto, TEMPLATE.privado.nome, False):
            print("-> Regra não permite contexto privado, mas contexto é privado. Regra não se aplica.")
            return False
    
        print("-> Regra se aplica!")
        return True

    def retornar_pontuacao(self):
        # print(f"[DEBUG - retornar_pontuacao] Regra {self.identificador}: punicao = {self.punicao}")
        return self.punicao


'''
    def __str__(self):
        cod = self.cod if self.cod else "Sem código"
        desc = self.desc if self.desc else "Sem descrição"
        return f"< Identificador {self.identificador} | Regra {cod} | Descrição: {desc}>"
    '''

'''
def retornar_pontuacao(self, contexto: dict):
    return getattr(contexto, TEMPLATE.reincidencia.nome, None) if self.prazo else getattr(contexto, TEMPLATE.punicao.nome, None)
'''
'''
def retornar_pontuacao(self, contexto: dict):
    valor = self.obter_valor(
        contexto,
        TEMPLATE.reincidencia.nome if self.prazo else TEMPLATE.punicao.nome,
        0
    )
    try:
        return int(valor)
    except (TypeError, ValueError):
        return 0
'''