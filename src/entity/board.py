from src.constants import COLOR_TILE_CLASS
from src.entity.house import House


class Board:
    def __init__(self, window):
        self.window = window
        self.player = window.player
        self.board_map = window.board_map
        self.first_dice = window.first_dice
        self.second_dice = window.second_dice
        self.throw_dice_popup = window.throw_dice_popup
        self.buy_house_popup = window.buy_house_popup
        self.throw_dice_popup.callback = self.throw_dice
        self.houses = {}
        self._load_houses()

    def _load_houses(self):
        color_tiles = self.board_map.positions[COLOR_TILE_CLASS]
        for color_tile in color_tiles:
            self.houses[color_tile] = House(int(color_tile), self.board_map)

    def start_game(self):
        self.throw_dice_popup.show()
        self.first_dice.dice_callback = self.on_dice_fall

    def on_dice_fall(self):
        self.player.next_step(self.first_dice.current_number() + self.second_dice.current_number())
        house = self.houses[str(self.player.position_index)]
        if house is None:
            self.throw_dice_popup.show()
        else:
            self.buy_house_popup.show_house(house)

    def throw_dice(self):
        self.first_dice.select_random_dice()
        self.second_dice.select_random_dice()
