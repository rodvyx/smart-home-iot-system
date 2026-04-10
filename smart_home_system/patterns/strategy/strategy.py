from abc import ABC, abstractmethod

class EnergyStrategy(ABC):

    @abstractmethod
    def optimize(self, devices: list):
        pass