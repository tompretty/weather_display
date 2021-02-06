from typing import Optional

from ...ui.widgets import Widget
from ..time import Time
from .base import Schedule


class ConstantSchedule(Schedule):
    """ConstantSchedule - A schedule that just shows a single widget.

    Parameters
    ----------
    start_time : Time
        the time at which this schedule starts being active
    end_time : Time
        the time at which this schedule stops being active
    widget: Widget
        the widget to show
    """

    def __init__(self, start_time: Time, end_time: Time, widget: Widget):
        super().__init__(start_time, end_time)
        self.widget = widget
        self.has_shown_widget = False

    def get_current_widget(self) -> Optional[Widget]:
        if self.has_shown_widget:
            return None
        self.has_shown_widget = True
        return self.widget

    def start(self):
        self.has_shown_widget = False
