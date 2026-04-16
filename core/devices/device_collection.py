from patterns.iterator.device_iterator import DeviceIterator

class DeviceCollection:

    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def create_iterator(self):
        return DeviceIterator(self._devices)