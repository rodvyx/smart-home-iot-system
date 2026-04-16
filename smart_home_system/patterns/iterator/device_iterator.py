from patterns.iterator.iterator import Iterator

class DeviceIterator(Iterator):

    def __init__(self, devices):
        self._devices = devices
        self._index = 0

    def has_next(self):
        return self._index < len(self._devices)

    def next(self):
        if self.has_next():
            device = self._devices[self._index]
            self._index += 1
            return device
        raise StopIteration