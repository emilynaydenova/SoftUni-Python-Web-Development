from abc import ABC, abstractmethod

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list = []  # list of peak.names
        self.is_prepared: bool = True  # has the required gear

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self) -> bool:
        # whether the climber has enough strength required to attempt a climb
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15.0

    def __str__(self):
        conquered_peaks = sorted(self.conquered_peaks)
        return (f"{type(self).__name__}: /// Climber name: {self.name} * "
                f"Left strength: {self.strength:.1f} * "
                f"Conquered peaks: {', '.join(conquered_peaks)} ///")
