from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120
    MISSED_TIME_TO_CATCH = 0.6

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.OXYGEN_LEVEL)

    # Decreases the diver's oxygen_level property.
    #  When the method is invoked the diver's oxygen_level is decreased by
    #  a certain value, that will depend on the fish
    # that is chased.
    def miss(self, time_to_catch: int):
        time_to_catch *= self.MISSED_TIME_TO_CATCH
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= time_to_catch
            self.oxygen_level = round(self.oxygen_level)

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL
        # self.has_health_issue = False
