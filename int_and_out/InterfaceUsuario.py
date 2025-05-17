from abc import ABC, abstractmethod

class InterfaceUsuario(ABC):
    """Interface abstrata para obter dados quando não estiverem no contexto."""

    @abstractmethod
    def solicitar_valor(self, nome: str) -> any:
        pass
