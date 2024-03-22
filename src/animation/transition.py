from abc import abstractmethod, ABC

import arcade


class MoveTransition(ABC):
    def __init__(self, animation_speed):
        self._start_x = 0
        self._start_y = 0
        self._target_x = 0
        self._target_y = 0
        self._animation_progress = 0
        self._animation_done = False
        self.animation_speed = animation_speed

    def update_animation(self):
        if self._animation_progress >= 1:
            self._animation_done = True
            self.update_position(self._target_x, self._target_y)
            return
        x = arcade.lerp(self._start_x, self._target_x, self._animation_progress)
        y = arcade.lerp(self._start_y, self._target_y, self._animation_progress)
        self.update_position(x, y)
        self._animation_progress += self.animation_speed

    def move(self, target_x, target_y):
        current_position = self.current_position()
        self._start_x = current_position[0]
        self._start_y = current_position[1]
        self._target_x = target_x
        self._target_y = target_y
        self._animation_progress = 0
        self._animation_done = False

    def is_animating(self):
        return not self._animation_done

    def _set_start_position(self, x, y):
        self._start_x = x
        self._start_y = y
        self._target_x = x
        self._target_y = y

    @abstractmethod
    def current_position(self) -> (float, float):
        pass

    @abstractmethod
    def update_position(self, x, y):
        pass
