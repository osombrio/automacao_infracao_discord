from dataclasses import dataclass
from typing import Optional, Union

from utils.template import TEMPLATE


@dataclass
class Regra:
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
    identificador: Optional[int] = None

    def gerar_template(self):
        cod = self.cod or "Sem código"
        desc = self.desc or "Sem descrição"
        return f"<Regra {cod} | Descrição: {desc}>"

    def se_aplica(self, contexto) -> bool:
        # Função auxiliar para pegar atributo de dict ou objeto
        def obter_valor(obj, chave, default=None):
            if isinstance(obj, dict):
                return obj.get(chave, default)
            return getattr(obj, chave, default)
    
        print(f"\nAvaliar regra: {self}")
    
        codigos_contexto = obter_valor(contexto, TEMPLATE.cod.nome, "")
        print(f"Códigos no contexto: {codigos_contexto}")
    
        if isinstance(codigos_contexto, str):
            codigos_contexto = [c.strip() for c in codigos_contexto.split(",")]
        elif not isinstance(codigos_contexto, list):
            codigos_contexto = [str(codigos_contexto)]

        cod = self.cod
        print(f"Códigos da regra: {cod}")
    
        if isinstance(cod, str):
            cod = [c.strip() for c in cod.split(",")]
        elif not isinstance(cod, list):
            cod = [str(cod)]
    
        # Verifica se algum código da regra está no contexto
        if not any(c in codigos_contexto for c in cod):
            print("-> Código da regra não corresponde ao contexto. Regra não se aplica.")
            return False
    
        # Pega a descrição (sem filtro condicao/exclusao)
        desc = (obter_valor(contexto, TEMPLATE.desc.nome, "") or "").lower()
        print(f"Descrição no contexto: '{desc}'")
    
        if self.prova and not obter_valor(contexto, TEMPLATE.prova.nome, False):
            print("-> Prova detalhada exigida, mas contexto não tem prova. Regra não se aplica.")
            return False
    
        if not self.intencao and not obter_valor(contexto, TEMPLATE.intencao.nome, False):
            print("-> Regra permite punir sem intenção, mas contexto indica ausência de intenção. Regra não se aplica.")
            return False
    
        if not self.privado and obter_valor(contexto, TEMPLATE.privado.nome, False):
            print("-> Regra não permite contexto privado, mas contexto é privado. Regra não se aplica.")
            return False
    
        print("-> Regra se aplica!")
        return True

    def retornar_pontuacao(self, contexto: dict):
        return getattr(contexto, TEMPLATE.reincidencia.nome, None) if self.prazo else getattr(contexto, TEMPLATE.punicao.nome, None)

    
    def __str__(self):
        cod = self.cod if self.cod else "Sem código"
        desc = self.desc if self.desc else "Sem descrição"
        return f"<Regra {cod} | Descrição: {desc}>"
    
