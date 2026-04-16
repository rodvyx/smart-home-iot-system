from services.device_service import DeviceService
from controllers.automation_controller import AutomationController

# Strategy
from patterns.strategy.concrete_strategies import CostSavingStrategy

# Command
from patterns.command.device_commands import TurnOffDevicesCommand

# Interpreter
from patterns.interpreter.context import Context
from patterns.interpreter.expressions import (
    EnergyGreaterThan,
    TurnOffCommand,
    IfThenExpression
)

# Decorator
from patterns.decorator.concrete_decorators import LoggingDecorator

# Adapter
from patterns.adapter.external_system import ExternalEnergyAPI
from patterns.adapter.adapter import EnergyAPIAdapter

# Memento
from patterns.memento.caretaker import Caretaker


def main():
    device_service = DeviceService()
    controller = AutomationController(device_service)
    caretaker = Caretaker()

    # Add devices
    device_service.add_device("meter", "Main Meter")
    device_service.add_device("thermostat", "Living Room Thermostat")

    # Save state
    caretaker.save(device_service.save())

    # Strategy (AI-like behavior)
    controller.set_strategy(CostSavingStrategy())
    print("Optimization:", controller.optimize())

    # Command execution
    command = TurnOffDevicesCommand([])
    print("Command:", controller.execute_command(command))

    # Interpreter (rule engine)
    context = Context(energy_value=6)
    rule = IfThenExpression(EnergyGreaterThan(5), TurnOffCommand())
    print("Rule Engine:", rule.interpret(context))

    # Decorator (monitoring)
    iterator = device_service.get_iterator()
    print("\nDecorated Devices:")
    while iterator.has_next():
        device = iterator.next()
        decorated = LoggingDecorator(device)
        print(decorated.get_status())

    # Adapter (external integration)
    api = EnergyAPIAdapter(ExternalEnergyAPI())
    print("\nExternal Data:", api.get_energy_data())

    # Restore state
    memento = caretaker.undo()
    if memento:
        device_service.restore(memento)

    print("\nSystem restored successfully")


if __name__ == "__main__":
    main()