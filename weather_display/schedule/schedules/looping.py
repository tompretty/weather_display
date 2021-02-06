from typing import List, Optional

from ...ui.widgets import Widget
from ..time import Time
from .base import Schedule


class LoopingSchedule(Schedule):
    """LoopingSchedule - A schedule that loops through a list of widgets.

    Parameters
    ----------
    start_time : Time
        the time at which this schedule starts being active
    end_time : Time
        the time at which this schedule stops being active
    widgets: List[Widget]
        the list of widgets to loop through
    """

    def __init__(self, start_time: Time, end_time: Time, widgets: List[Widget]) -> None:
        super().__init__(start_time, end_time)
        self.widgets = widgets
        self.current_widget_index = 0

    def get_current_widget(self) -> Optional[Widget]:
        current_widget = self.widgets[self.current_widget_index]
        self.increment_current_widget_index()
        return current_widget

    def start(self) -> None:
        self.current_widget_index = 0

    def increment_current_widget_index(self):
        self.current_widget_index = (self.current_widget_index + 1) % len(self.widgets)
