import napari
from qtpy.QtCore import QTimer
from qtpy.QtWidgets import QWidget


class Napari(QWidget):
    def __init__(self, viewer: napari.Viewer):
        super().__init__()
        self._viewer = viewer
        self._timer = QTimer()
        self._timer.timeout.connect(self._update_napari)

        self._napari = self._viewer.add_image(
            self._viewer.screenshot(canvas_only=False, flash=False),
            rgb=True,
            name="napari",
        )

        self._timer.start()

    def _update_napari(self) -> None:
        self._napari.data = self._viewer.screenshot(
            canvas_only=False, flash=False
        )
