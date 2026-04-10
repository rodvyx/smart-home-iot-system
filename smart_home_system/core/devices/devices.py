from core.devices.base_device import SmartDevice
import copy

class SmartMeter(SmartDevice):
    def get_status(self) -> str:
        return f"{self.name}: Measuring energy consumption"

    def clone(self, name: str):
        new_obj = copy.copy(self)
        new_obj.name = name
        return new_obj


class Thermostat(SmartDevice):
    def __init__(self, name: str, temperature: float = 22.0):
        super().__init__(name)
        self.temperature = temperature

    def get_status(self) -> str:
        return f"{self.name}: Temperature set to {self.temperature}°C"

    def clone(self, name: str):
        new_obj = copy.copy(self)
        new_obj.name = name
        return new_obj


class SolarPanel(SmartDevice):
    def __init__(self, name: str, capacity: float = 5.0):
        super().__init__(name)
        self.capacity = capacity

    def get_status(self) -> str:
        return f"{self.name}: Capacity {self.capacity}kW"

    def clone(self, name: str):
        new_obj = copy.copy(self)
        new_obj.name = name
        return new_obj