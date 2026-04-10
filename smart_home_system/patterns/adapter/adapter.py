class EnergyAPIAdapter:
    def __init__(self, external_api):
        self.external_api = external_api

    def get_energy_data(self):
        return self.external_api.fetch_data()