import arcade


class Player:
    def __init__(self, board, radius, position_index=0, money=0):
        self.board = board
        self.radius = radius
        self.money = money
        self.position_index = position_index

    def draw(self):
        x, y = self.board.index_to_position(self.position_index)
        arcade.draw_circle_filled(x, y, self.radius, arcade.color.GOLD)
