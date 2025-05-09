import os
from PySide6.QtCore import QTimer, QUrl, QEvent, Qt
from PySide6.QtGui import QMouseEvent
from .base_state import PetState, StateHandler


class ClickedStateHandler(StateHandler):
    """点击状态处理器"""

    def _init_state(self):
        self.pet_window.audio_player.setSource(
            QUrl.fromLocalFile(self.pet_window.click_mp3_path)
        )
        self.pet_window.audio_player.stop()
        return super()._init_state()

    def on_enter(self):
        self.pet_window.play_gif(self.pet_window.click_gif_path)
        if os.path.exists(self.pet_window.click_mp3_path):
            self.pet_window.audio_player.setSource(
                QUrl.fromLocalFile(self.pet_window.click_mp3_path)
            )
            self.pet_window.audio_player.play()
        QTimer.singleShot(18000, self._on_click_end)  # type: ignore[call-arg-type]

    def on_exit(self):
        self.pet_window.audio_player.stop()
        return False

    def handle_event(self, event: QEvent) -> bool:
        if isinstance(event, QMouseEvent):
            if event.type() == QEvent.Type.MouseButtonPress:
                return self._handle_mouse_press(event)
        return False

    def update_config(self):
        return super().update_config()

    def _handle_mouse_press(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.state_machine.transition_to(PetState.DRAGGING)
            return True
        return False

    def _on_click_end(self):
        """点击动画结束"""
        self.state_machine.pop_state()
