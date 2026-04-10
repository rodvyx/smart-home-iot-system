from abc import ABC, abstractmethod
from core.devices.base_device import SmartDevice

class DeviceFactory(ABC):

    @abstractmethod
    def create_device(self, name: str) -> SmartDevice:
        pass