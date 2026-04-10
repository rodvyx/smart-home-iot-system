from patterns.decorator.device_decorator import DeviceDecorator


class LoggingDecorator(DeviceDecorator):
    def get_status(self):
        return f"[LOG] {self._device.get_status()}"


class AlertDecorator(DeviceDecorator):
    def get_status(self):
        return f"[ALERT] {self._device.get_status()}"