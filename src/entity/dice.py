import random

import arcade

from src.constants import DICE_SCALE


class Dice:
    def __init__(self, dices_path, position):
        self.first = self._create_dice(dices_path + 'first.png', position)
        self.second = self._create_dice(dices_path + 'second.png', position)
        self.third = self._create_dice(dices_path + 'third.png', position)
        self.fourth = self._create_dice(dices_path + 'fourth.png', position)
        self.fifth = self._create_dice(dices_path + 'fifth.png', position)
        self.sixth = self._create_dice(dices_path + 'sixth.png', position)
        self.dices_indexes = {1: self.first, 2: self.second, 3: self.third, 4: self.fourth, 5: self.fifth, 6: self.sixth}
        self.current = self.select_random_dice()

    def draw(self):
        self.current[1].draw()

    def current_number(self):
        return self.current[0]

    def select_random_dice(self):
        random_dice = random.choice(list(self.dices_indexes.items()))
        self.current = random_dice
        return random_dice

    @staticmethod
    def _create_dice(path, position):
        dice = arcade.Sprite(path, DICE_SCALE)
        dice.center_x = position[0]
        dice.center_y = position[1]
        return dice
