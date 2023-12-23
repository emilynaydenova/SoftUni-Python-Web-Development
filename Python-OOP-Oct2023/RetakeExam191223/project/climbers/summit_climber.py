from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    MINIMUM_STRENGTH_TO_CLIMB = 75

    def __init__(self, name: str):
        super().__init__(name, strength= self.INITIAL_STRENGTH)

    def can_climb(self):
        # the climber's strength is greater than or equal to the specified
        # minimum strength to climb
        return self.strength >= self.MINIMUM_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == 'Advanced':
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5
        self.conquered_peaks.append(peak.name)
