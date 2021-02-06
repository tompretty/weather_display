from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from ...ui.widgets import Widget
from ..time import Time


class Schedule(ABC):
    """Schedule - A base class for schedules

    Schedules handle the logic for deciding which widget should be shown at
    the current moment in time. The have a `start_time` and `end_time` which
    dictate when they are considered active.

    Parameters
    ----------
    start_time : Time
        the time at which this schedule starts being active
    end_time : Time
        the time at which this schedule stops being active
    """

    def __init__(self, start_time: Time, end_time: Time) -> None:
        self.start_time = start_time
        self.end_time = end_time

    @abstractmethod
    def get_current_widget(self) -> Optional[Widget]:
        """Get the current widget to display.

        A return type of `None` indicates that the display shouldn't be
        updated.

        Returns
        -------
        Optional[Widget]
            the widget to display
        """
        raise NotImplementedError

    def is_active(self) -> bool:
        """Get the activate status of the schedule.

        Returns
        -------
        bool
            whether or not the schedule is active
        """
        now = datetime.now()
        current_time = Time(hours=now.hour, minutes=now.minute)
        is_after_start = current_time.is_after(self.start_time)
        is_before_end = current_time.is_before(self.end_time)
        return is_after_start and is_before_end

    def start(self) -> None:
        """Start the schedule.

        Schedules can use this to reset any required internal state.
        """
        pass
