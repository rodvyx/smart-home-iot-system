from services.energy_service import EnergyService
from services.command_service import CommandService

class AutomationController:

    def __init__(self, device_service):
        self.device_service = device_service
        self.energy_service = EnergyService(None)
        self.command_service = CommandService()

    def set_strategy(self, strategy):
        self.energy_service.set_strategy(strategy)

    def optimize(self):
        iterator = self.device_service.get_iterator()
        devices = []

        while iterator.has_next():
            devices.append(iterator.next())

        return self.energy_service.optimize_energy(devices)

    def execute_command(self, command):
        return self.command_service.execute_command(command)