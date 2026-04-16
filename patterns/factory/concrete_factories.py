from patterns.factory.device_factory import DeviceFactory
from core.devices.devices import SmartMeter, Thermostat, SolarPanel

class SmartMeterFactory(DeviceFactory):
    def create_device(self, name: str):
        return SmartMeter(name)


class ThermostatFactory(DeviceFactory):
    def create_device(self, name: str):
        return Thermostat(name)


class SolarPanelFactory(DeviceFactory):
    def create_device(self, name: str):
        return SolarPanel(name)