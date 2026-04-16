from abc import ABC, abstractmethod
from patterns.prototype.prototype import Prototype

class SmartDevice(Prototype):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_status(self) -> str:
        pass

    @abstractmethod
    def clone(self, name: str):
        pass