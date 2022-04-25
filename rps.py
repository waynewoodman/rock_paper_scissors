#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# moves = ['rock', 'paper', 'scissors']

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

    def beats(player_decision, computer_decision):
        if player_decision != computer_decision:
            return ((player_decision == 'rock' and computer_decision ==
                     'scissors')
                    or (player_decision == 'scissors' and computer_decision
                    == 'paper')
                    or (player_decision == 'paper' and computer_decision ==
                    'rock'))


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


class CyclePlayer(Player):
    def move(self, rounds):
        index = (rounds - 1) % 3
        if index == 0:
            random.shuffle(self.moves)
            return self.moves[index]
        else:
            return self.moves[index]

            class Game:
            def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2
            self.game_count = 0

            def track_score(self, move1, move2):
            score = Player.beats(move1, move2)
            if score == 1:
            self.p1.count += 1
            elif score == 0:
            self.p2.count += 1
            else:
            return
            print("\tScore: " + str(self.p1.count) + " _ "
                  + str(self.p2.count))

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
            computer_classes = (Player(), RandomPlayer(), ReflectPlayer(),
                                CyclePlayer())
            computer_player = random.choice(computer_classes)
            game = Game(HumanPlayer(), computer_player)
            game.play_game()
