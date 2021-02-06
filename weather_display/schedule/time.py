class Time:
    """Time - Represents a time of day as an hours, minutes pair.

    Parameters
    ----------
    hours : int
        the hour
    minutes : int
        the minutes
    """

    def __init__(self, hours: int, minutes: int) -> None:
        self.hours = hours
        self.minutes = minutes

    def is_before(self, other_time: "Time") -> bool:
        return self.total_minutes() < other_time.total_minutes()

    def is_after(self, other_time: "Time") -> bool:
        return self.total_minutes() > other_time.total_minutes()

    def total_minutes(self) -> int:
        return self.hours * 60 + self.minutes

