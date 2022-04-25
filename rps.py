#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.count = 0
        self.computer_move = ""

    def learn(self, my_move, computer_move):
        self.computer_move = computer_move
        self.my_move = my_move

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors')
                or (one == 'scissors' and two == 'paper')
                or (one == 'paper' and two == 'rock'))

class HumanPlayer(Player):
    def move(self, rounds):
        self.select_move = input("Rock, paper, scissors?\n").lower()
        for options in self.moves:
            if self.select_move in self.moves:
                return self.select_move
            else:
                self.move(rounds)

class ReflectPlayer(Player):
    def move(self, rounds):
        if rounds == 1:
            return random.choice(self, rounds)
        else:
            return self.computer_move


class RandomPlayer():
    def move(self, rounds):
        return random.choice(self.moves)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def track_score(self):
        score = Player.beats(move1, move2):
            if score == 1:
                self.p1.count+= 1
            elif: score == 0:
                self.p2.count += 1
            else:
                return

    def play_round(self):
        self.game_count += 1
        games = self.game_count
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.track_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
