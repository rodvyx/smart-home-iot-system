from patterns.prototype.registry import DeviceRegistry
from core.devices.device_collection import DeviceCollection
from patterns.memento.memento import Memento
from patterns.factory.concrete_factories import (
    SmartMeterFactory,
    ThermostatFactory,
    SolarPanelFactory
)

class DeviceService:

    def __init__(self):
        self.collection = DeviceCollection()
        self.registry = DeviceRegistry()
        self._initialize_prototypes()
    
    def save(self):
        # Save current device list
        state = list(self.collection._devices)
        return Memento(state)
    
    def restore(self, memento: Memento):
        self.collection._devices = memento.get_state()

    def _initialize_prototypes(self):
        meter = SmartMeterFactory().create_device("Default Meter")
        thermostat = ThermostatFactory().create_device("Default Thermostat")
        solar = SolarPanelFactory().create_device("Default Solar")

        self.registry.register("meter", meter)
        self.registry.register("thermostat", thermostat)
        self.registry.register("solar", solar)

    def add_device(self, device_type: str, name: str):
        device = self.registry.clone(device_type, name)
        self.collection.add_device(device)

    def get_iterator(self):
        return self.collection.create_iterator()