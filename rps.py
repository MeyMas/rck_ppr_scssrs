import random
moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0
        self.my_move = None
        self.their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            self.my_move = input("\tYour Choice Is? >>>\n\t").lower()
            while self.my_move in moves:
                return self.my_move
            print("Sorry, Please try again. =>\n")


class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2,):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"    {move1.capitalize()} vs {move2.capitalize()}")
        if beats(move1, move2) is True:
            self.p1.score += 1
            print(f"{move1.upper()} beats {move2.capitalize()}\n"
                  "===================================")
        elif beats(move2, move1) is True:
            self.p2.score += 1
            print(f"{move1.capitalize()} looses to {move2.upper()}\n"
                  "===================================")
        else:
            print("\tYou tied\n===================================")
        print(f"Score: Player One: {self.p1.score}, "
              f"Player Two: {self.p2.score}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, a, z):
        print("Game start!")
        for round in range(a, z):     # "Roound 1" at the start looks
            print(f"Round {round}:")  # better than "Round 0"
            self.play_round()
        if self.p1.score > self.p2.score:
            print("Player One won!")
        elif self.p2.score > self.p1.score:
            print("Player Two won!")
        else:
            print("It was a tie.")
        print(f"Game over! The final score is "
              f"{self.p1.score} -- {self.p2.score}")


if __name__ == '__main__':
    random_player = random.choice([Player(), RandomPlayer(),
                                  ReflectPlayer(), CyclePlayer()])
    game = Game(HumanPlayer(), random_player)
    game.play_game(1, 4)
