class EnergyService:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def optimize_energy(self, devices):
        return self.strategy.optimize(devices)