from nicegui import ui

from .. import optional_features
from ..logging import log

try:
    from nicegui_highcharts import highchart
    optional_features.register('highcharts')
    __all__ = ['highchart']
except ImportError:
    class highchart(ui.element):  # type: ignore
        def __init__(self, *args, **kwargs) -> None:
            """Highcharts chart

            An element to create a chart using `Highcharts <https://www.highcharts.com/>`_.
            Updates can be pushed to the chart by changing the `options` property.
            After data has changed, call the `update` method to refresh the chart.

            Due to Highcharts' restrictive license, this element is not part of the standard NiceGUI package.
            It is maintained in a `separate repository <https://github.com/zauberzeug/nicegui-highcharts/>`_
            and can be installed with `pip install nicegui[highcharts]`.
            """
            super().__init__()
            ui.markdown('Highcharts is not installed. Please run `pip install nicegui[highcharts]`.')
            log.warning('Highcharts is not installed. Please run "pip install nicegui[highcharts]".')
