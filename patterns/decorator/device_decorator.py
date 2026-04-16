from core.devices.base_device import SmartDevice

class DeviceDecorator(SmartDevice):
    def __init__(self, device: SmartDevice):
        self._device = device

    def get_status(self):
        return self._device.get_status()

    def clone(self, name: str):
        return self._device.clone(name)