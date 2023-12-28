from qgis.gui import (
    QgsDockWidget,
    QgsFilterLineEdit
)


from qgis.PyQt import uic

# Module imports
from .gui_utils import GuiUtils
from .svg_label import SvgLabel
# from .context_widget import (
#     ContextItemMenuAction,
#     ContextLogo,
#     NoMouseReleaseMenu
# )

WIDGET, _ = uic.loadUiType(GuiUtils.get_ui_file_path('koordinates.ui'))


class CivicSimGui(QgsDockWidget, WIDGET):
    TAB_STARRED_INDEX = 1
    TAB_EXPLORE_INDEX = 0
    TAB_CONTEXT_SWITCHER_INDEX = 3

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        # self.logo_widget = SvgLabel('koordinates_logo.svg', 110, ContextLogo.LOGO_HEIGHT)
        self.logo_widget = SvgLabel('koordinates_logo.svg', 110, 55)

