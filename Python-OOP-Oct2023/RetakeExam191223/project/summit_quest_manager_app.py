from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS_TYPE = {
        'ArcticClimber': ArcticClimber,
        'SummitClimber': SummitClimber,
    }
    VALID_PEAKS_TYPE = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak,
    }

    def __init__(self):
        self.climbers = []  # climber objects
        self.peaks = []  # peak objects

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS_TYPE:
            return f"{climber_type} doesn't exist in our register."
        if [c for c in self.climbers if c.name == climber_name]:
            return f"{climber_name} has been already registered."

        new_climber = self.VALID_CLIMBERS_TYPE[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS_TYPE:
            return f"{peak_type} is an unknown type of peak."
        # can be doubled ???
        new_peak = self.VALID_PEAKS_TYPE[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = [c for c in self.climbers if c.name == climber_name][0]
        peak = [p for p in self.peaks if p.name == peak_name][0]

        needed_gear = set(peak.get_recommended_gear())
        missing_gear = needed_gear - set(gear)

        if missing_gear:
            climber.is_prepared = False
            missing_gear = sorted(missing_gear)
            return (f"{climber_name} is not prepared to climb {peak_name}. "
                    f"Missing gear: {', '.join(missing_gear)}.")

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        # the climber to conquer a specific peak
        climber = [c for c in self.climbers if c.name == climber_name]
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        climber = climber[0]

        peak = [p for p in self.peaks if p.name == peak_name]
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        peak = peak[0]

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."


    def get_statistics(self):

        successfully_climbers = [c for c in self.climbers if c.conquered_peaks]
        sorted_climbers = sorted(successfully_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))

        result = [f"Total climbed peaks: {len(self.peaks)}",
                  "**Climber's statistics:**"]

        for c in sorted_climbers:
            result.append(str(c))
        return "\n".join(result)
