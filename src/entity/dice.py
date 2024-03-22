import random
from datetime import datetime, timedelta

import arcade

from src.constants import UPDATES_PER_FRAME


class Dice:
    def __init__(self, dices_path, animated_dices_path, position):
        self.first = self._create_dice(dices_path + 'first.png', position)
        self.second = self._create_dice(dices_path + 'second.png', position)
        self.third = self._create_dice(dices_path + 'third.png', position)
        self.fourth = self._create_dice(dices_path + 'fourth.png', position)
        self.fifth = self._create_dice(dices_path + 'fifth.png', position)
        self.sixth = self._create_dice(dices_path + 'sixth.png', position)
        self.dices_indexes = {1: self.first, 2: self.second, 3: self.third, 4: self.fourth, 5: self.fifth,
                              6: self.sixth}
        self.current = (1, self.dices_indexes[1])

        self.animated_dices = [
            arcade.Sprite(animated_dices_path + "first.png"),
            arcade.Sprite(animated_dices_path + "sixth.png"),
            arcade.Sprite(animated_dices_path + "fifth.png"),
            arcade.Sprite(animated_dices_path + "fourth.png"),
            arcade.Sprite(animated_dices_path + "third.png"),
            arcade.Sprite(animated_dices_path + "second.png")
        ]
        random.shuffle(self.animated_dices)
        for animated_dice in self.animated_dices:
            animated_dice.center_x = position[0]
            animated_dice.center_y = position[1]

        self.rolling = False
        self.current_texture = 0
        self.current_time = None
        self.rolling_sprite = self.animated_dices[1]


    def draw(self):
        if self.rolling:
            self.rolling_sprite.draw()
        else:
            self.current[1].draw()

    def update(self, delta_time):
        if self.rolling:
            self.current_texture += 1
            if self.current_texture > 5 * UPDATES_PER_FRAME:
                self.current_texture = 0
            frame = self.current_texture // UPDATES_PER_FRAME
            self.rolling_sprite = self.animated_dices[frame]
            end_time = self.current_time + timedelta(seconds=1)
            if datetime.now() > end_time:
                self.rolling = False

    def current_number(self):
        return self.current[0]

    def select_random_dice(self):
        self.rolling = True
        self.current_time = datetime.now()
        self.current = random.choice(list(self.dices_indexes.items()))

    @staticmethod
    def _create_dice(path, position):
        dice = arcade.Sprite(path)
        dice.center_x = position[0]
        dice.center_y = position[1]
        return dice
