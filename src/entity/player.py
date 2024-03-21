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

    def next_step(self, amount):
        new_position = self.position_index + amount
        if new_position not in self.board.positions:
            self.position_index = new_position % len(self.board.positions)
            return
        self.position_index += amount
