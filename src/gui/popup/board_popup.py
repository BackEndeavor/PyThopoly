import arcade.gui

from src.constants import UI_POPUP_CLASS


class BasePopup:
    def __init__(self, board_map, ui_manager, index):
        self.board_map = board_map
        self.ui_manager = ui_manager
        rectangle = self.board_map.find_position(UI_POPUP_CLASS, index)
        self.x, self.y, self.width, self.height = rectangle
        self.y -= self.height
        self.layout = arcade.gui.UILayout(self.x, self.y, self.width, self.height)

    def show(self):
        self.ui_manager.add(self.layout)

    def hide(self):
        self.ui_manager.remove(self.layout)


class ThrowDicePopup(BasePopup):
    def __init__(self, ui_manager, board_map, callback=None):
        super().__init__(board_map, ui_manager, '0')
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


class BuyHousePopup(BasePopup):
    def __init__(self, ui_manager, board_map, callback=None):
        super().__init__(board_map, ui_manager, '0')
        self.callback = callback

    def on_house_buy(self, button, house):
        self.callback(button == "Отказаться", house)

    def show_house(self, house):
        def on_house_buy(button):
            self.on_house_buy(button, house)

        message_box = arcade.gui.UIMessageBox(
            width=self.width,
            height=self.height,
            message_text=(
                "Хотите купить дом?"
            ),
            buttons=["Купить", "Отказаться"],
            callback=on_house_buy
        )
        self.layout.add(message_box)

        super().show()
