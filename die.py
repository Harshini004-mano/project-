import random
class Dice:
    def roll(self):
        return random.randint(1, 6)

class Token:
    def __init__(self):
        self.position = 0  # 0 = start, target = 100 (finish)
        self.finished = False

    def move(self, steps):
        if not self.finished:
            self.position += steps
            if self.position >= 100:  # assuming 100 is finish
                self.position = 100
                self.finished = True

class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = [Token() for _ in range(4)]

    def all_tokens_finished(self):
        return all(token.finished for token in self.tokens)

class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.dice = Dice()
        self.current_player = 0

    def play_turn(self):
        player = self.players[self.current_player]
        roll = self.dice.roll()
        print(f"{player.name} rolled a {roll}")
        # For simplicity, move the first token not finished
        for token in player.tokens:
            if not token.finished:
                token.move(roll)
                break
        self.display_board()
        if player.all_tokens_finished():
            print(f"{player.name} has won!")
            return True
        # Next player's turn
        self.current_player = (self.current_player + 1) % len(self.players)
        return False

    def display_board(self):
        for player in self.players:
            positions = [token.position for token in player.tokens]
            print(f"{player.name}: {positions}")

# Example of running the game
game = Game(["Alice", "Bob"])
winner = False
while not winner:
    winner = game.play_turn()