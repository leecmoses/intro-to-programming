#!/usr/bin/env python3

import random
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
        print("What would you like to throw?")
        throw = input("> ").lower()
        while throw not in moves:
            print("Please enter a valid throw: rock, paper, or scissors")
            throw = input("> ").lower()
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
        self.cycle = moves[:]

    def move(self):
        if len(self.cycle) > 0:
            return self.cycle.pop(0)
        else:
            self.cycle = moves[:]
            return self.cycle.pop(0)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def SelectPlayer():
        player = ''
        players = ['random', 'reflect', 'repeat', 'cycle']
        print("Who would you like to play with?")
        while player not in players:
            print("Please enter 'random', 'reflect', 'repeat' or 'cycle'")
            player = input("> ").lower()
        if player == 'random':
            return RandomPlayer()
        elif player == 'reflect':
            return ReflectPlayer()
        elif player == 'repeat':
            return RepeatPlayer()
        elif 'cycle':
            return CyclePlayer()


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("The round is a tie!")
        elif beats(move1, move2):
            print("You won the round!")
            self.p1.score += 1
        else:
            print("Computer won the round!")
            self.p2.score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        rounds = 0
        print("How many rounds do you want to play?")
        while rounds <= 0:
            try:
                print("Enter number of rounds")
                rounds = int(input("> "))
            except ValueError:
                print("Please enter a number")
                rounds = int(input("> "))
        print("Here are the rules to the game: scissor cuts paper,"
              " paper covers rock, and rock crushes scissors")
        print("Play either rock, paper, or scissors")
        for round in range(1, rounds + 1):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            self.final_score = self.p1.score
            self.winner = 'You'
        elif self.p2.score > self.p1.score:
            self.final_score = self.p2.score
            self.winner = 'Computer'
        else:
            print(f"Wow! It's a tie!")
        print(f"{self.winner} won with the game {self.final_score} point(s)!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), SelectPlayer())
    game.play_game()
