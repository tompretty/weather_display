import time
from typing import List, Optional

from ..ui.widgets import Widget
from .schedules import Schedule


class Scheduler:
    """Scheduler

    Parameters
    ----------
    schedules : List[Schedule]
        the list of schedules
    shchedule_interval: int
        the time between updates
    """

    def __init__(self, schedules: List[Schedule], schedule_interval: int):
        self.schedules = schedules
        self.previous_schedule = None  # type: Optional[Schedule]
        self.schedule_interval = schedule_interval

    def get_current_widget(self) -> Optional[Widget]:
        """Get the current widget to display.

        A return value of `None` indicates the display shouldn't update.

        Returns
        -------
        Optional[Widget]
            the widget to display
        """
        current_schedule = self._get_current_schedule()
        if not current_schedule:
            return None
        elif current_schedule is not self.previous_schedule:
            current_schedule.start()
        self.previous_schedule = current_schedule
        return current_schedule.get_current_widget()

    def _get_current_schedule(self) -> Optional[Schedule]:
        for schedule in self.schedules:
            if schedule.is_active():
                return schedule
        return None

    def _sleep_until_next_update(self):
        time.sleep(self.schedule_interval)
