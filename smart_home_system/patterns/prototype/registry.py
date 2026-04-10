class DeviceRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, key: str, prototype):
        self._prototypes[key] = prototype

    def clone(self, key: str, name: str):
        prototype = self._prototypes.get(key)

        if not prototype:
            raise ValueError("Prototype not found")

        return prototype.clone(name)