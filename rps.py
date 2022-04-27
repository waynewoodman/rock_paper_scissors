import random
import time


def print_pause(message_display):
    print(message_display)
    time.sleep(1)


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.count = 0
        self.computer_move = ""
        self.my_move = self.moves

    def move(self, rounds):
        return "rock"

    def learn(self, my_move, computer_move):
        self.computer_move = computer_move
        self.my_move = my_move

    def beats(player_decision, computer_decision):
        if player_decision != computer_decision:
            return ((player_decision == 'rock' and computer_decision
                     == 'scissors')
                    or (player_decision == 'scissors' and computer_decision
                    == 'paper')
                    or (player_decision == 'paper' and computer_decision
                    == 'rock'))
        else:
            return 2


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
        return self.computer_move


class RandomPlayer(Player):
    def move(self, rounds):
        return random.choice(self.moves)


class CyclePlayer(Player):
    def move(self, rounds):
        index = (rounds - 1) % 3
        index == 0
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
        print_pause("\tScore: " + str(self.p1.count) + " _ "
                    + str(self.p2.count))

    def play_round(self):
        self.game_count += 1
        rounds = self.game_count
        print_pause(f"\nRound {rounds}:")
        move1 = self.p1.move(rounds)
        move2 = self.p2.move(rounds)
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        self.track_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("Rock, Paper, Scissors, lets play!")
        total_rounds = input("Please state how many games you would like to "
                             "play?\n")
        try:
            print_pause("\nGreat, lets go!")
            for round in range(int(total_rounds)):
                self.play_round()
            self.winner()
            print_pause("\tFinal Score: " + str(self.p1.count) + " _ "
                        + str(self.p2.count))
            print_pause("Game, set, match!")
        except ValueError:
            game.play_game()

    def winner(self):
        if self.p1.count > self.p2.count:
            print_pause("Player wins!")
        elif self.p1.count < self.p2.count:
            print_pause("Computer wins!")
        else:
            print_pause("Its a tie :)")


if __name__ == '__main__':
    player_classes = (Player(), RandomPlayer(), ReflectPlayer(),
                      CyclePlayer())

    computer_player = random.choice(player_classes)
    game = Game(HumanPlayer(), computer_player)
    game.play_game()
