from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540
    MISSED_TIME_TO_CATCH = 0.3

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        time_to_catch *= self.MISSED_TIME_TO_CATCH
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= time_to_catch
            self.oxygen_level = round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL

