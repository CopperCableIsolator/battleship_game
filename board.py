import random as rand

WATER = 0
SHIP = 1
SIZE = 10
HIT_REWARD = 1
SUNK_REWARD = 10


class Board:

    def __init__(self):
        self.BOARD = [[WATER for i in range(SIZE)] for i in range(SIZE)]
        self.SHIP_POSITIONS = []
        self.SCORE = 0

    def generate_ship_positions(self, boat_size: int):
        # checks if a valid position is found and places accordingly.
        # returns True if position was filled
        position = [rand.randint(0, SIZE - boat_size), rand.randint(0, SIZE - boat_size)]
        orientation = rand.randint(0, 1)
        ship_position = []
        position_free = True

        for i in range(position[orientation], position[orientation] + boat_size):
            if self.BOARD[position[1]*(orientation ^ 1) + i * orientation][position[0] * orientation + i * (orientation ^ 1)] == SHIP:
                position_free = False

        if position_free:
            for i in range(position[orientation], position[orientation] + boat_size):
                self.BOARD[position[1]*(orientation ^ 1) + i * orientation][position[0] * orientation + i * (orientation ^ 1)] = SHIP
                ship_position.append([position[1]*(orientation ^ 1) + i * orientation, position[0] * orientation + i * (orientation ^ 1)])
            self.SHIP_POSITIONS.append(ship_position)
            return True

    def place_ships(self, *args):
        ships = list(args)
        i = 0
        while i < ships.__len__():
            if self.generate_ship_positions(ships[i]):
                i += 1

    def ship_destroyed(self, strike):
        proxy_list = self.SHIP_POSITIONS
        i = 0
        while i < proxy_list.__len__():
            if strike in proxy_list[i]:
                proxy_list[i].remove(strike)
                self.SCORE += HIT_REWARD
            if not proxy_list[i]:
                del proxy_list[i]
                self.SCORE += SUNK_REWARD
                continue
            i += 1
        self.SHIP_POSITIONS = proxy_list


class Player:

    def __init__(self, board: []):
        self.SCORE = 0
        self.BOARD = board
        self.OVERLAY = [["-" for i in range(SIZE)] for i in range(SIZE)]

    def player_input(self, y_guess: int, x_guess: int):
        if self.BOARD[y_guess][x_guess] == SHIP:
            self.OVERLAY[y_guess][x_guess] = "O"
            self.SCORE += 1
        else:
            self.OVERLAY[y_guess][x_guess] = "X"


g = Board()
g.place_ships(4, 4, 4, 4)
print(g.SHIP_POSITIONS)
g.ship_destroyed([1, 2])
print(g.SCORE)
print(g.SHIP_POSITIONS)

p = Player(g.BOARD)
a = "  "

for i in g.BOARD:
    print(i)
