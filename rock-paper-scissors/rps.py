#!/usr/bin/env python3

import random
from colorama import Fore, Style
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.score = 0

    def learn(self, my_move, their_move):
        self.my_move, self.their_move = my_move, their_move


class HumanPlayer(Player):

    def move(self):
        throw = ''
        while throw not in moves:
            print("Rock, paper, or scissors?")
            throw = input(">>> ").lower()
        return throw


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):

    def __init__(self):
        super().__init__()
        self.my_move = ''
        self.their_move = ''

    def move(self):
        if self.their_move:
            return self.their_move
        else:
            return random.choice(moves)


class RepeatPlayer(Player):

    def move(self):
        return "rock"


class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.cycle = -1

    def move(self):
        self.cycle += 1
        if self.cycle % 3 == 0:
            return moves[0]
        elif self.cycle % 3 == 1:
            return moves[1]
        elif self.cycle % 3 == 2:
            return moves[2]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def select_player():
    player = ''
    players = ['random', 'reflect', 'repeat', 'cycle']
    while player not in players:
        print("Select mode: random, reflect, repeat, or cycle")
        player = input(">>> ").lower()
    if player == 'random':
        return RandomPlayer()
    elif player == 'reflect':
        return ReflectPlayer()
    elif player == 'repeat':
        return RepeatPlayer()
    elif player == 'cycle':
        return CyclePlayer()


def select_rounds():
    rounds = 0
    while integer_validation(rounds) is False:
        print("How many rounds?")
        rounds = input(">>> ")
    rounds = int(rounds)
    return rounds


def integer_validation(value):
    try:
        return int(value) > 0
    except ValueError:
        return False


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(Fore.RED + f"You played {move1}.")
        print(Fore.BLUE + f"Opponent played {move2}." + Style.RESET_ALL)
        if move1 == move2:
            print("The round is a tie!")
        elif beats(move1, move2):
            print("You won the round!")
            self.p1.score += 1
        else:
            print("Opponent won the round!")
            self.p2.score += 1
        print(f"Score: {self.p1.score} - {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        for round in range(1, select_rounds() + 1):
            print(Fore.YELLOW + f"\n-- Round {round} --" + Style.RESET_ALL)
            self.play_round()
        if self.p1.score > self.p2.score:
            print(Fore.YELLOW +
                  f"\nYou won the game with {self.p1.score} point(s)!")
        elif self.p2.score > self.p1.score:
            print(Fore.YELLOW +
                  f"\nOpponent won the game with {self.p2.score} point(s)!")
        else:
            print(Fore.YELLOW +
                  f"\nYou and the opponent tied! Play again!")


if __name__ == '__main__':
    print("Rock Paper Scissors, Shoot!")
    game = Game(HumanPlayer(), select_player())
    game.play_game()
