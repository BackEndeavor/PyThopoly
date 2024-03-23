import arcade.gui

from src.constants import UI_POPUP_CLASS


class BasePopup:
    def __init__(self, board, ui_manager, index):
        self.board = board
        self.ui_manager = ui_manager
        rectangle = self.board.find_position(UI_POPUP_CLASS, index)
        self.x, self.y, self.width, self.height = rectangle
        self.y -= self.height
        self.layout = arcade.gui.UILayout(self.x, self.y, self.width, self.height)

    def show(self):
        self.ui_manager.add(self.layout)

    def hide(self):
        self.ui_manager.remove(self.layout)


class ThrowDicePopup(BasePopup):
    def __init__(self, ui_manager, board, callback):
        super().__init__(board, ui_manager, '0')
        self.callback = callback

    def on_dice_throw(self, button):
        self.callback()

    def show(self):
        self.layout.add(arcade.gui.UIMessageBox(
            width=self.width,
            height=self.height,
            message_text=(
                "Ваш ход!"
            ),
            buttons=["Бросить кубики"],
            callback=self.on_dice_throw
        ))
        super().show()



