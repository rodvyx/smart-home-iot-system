class TurnOffDevicesCommand:
    def __init__(self, devices):
        self.devices = devices

    def execute(self):
        return "Turning off all devices"


class ActivateEcoModeCommand:
    def execute(self):
        return "Activating eco mode"


class StartOptimizationCommand:
    def execute(self):
        return "Starting energy optimization"