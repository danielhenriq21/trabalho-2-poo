# Definição da classe abstrata Person que serve de base para User
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_details(self):
        pass
