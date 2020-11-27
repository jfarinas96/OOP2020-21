# Author: Janae Fariñas
# Date: 27-11-2020
# Purpose: Using an abstract class to facilitate a maths game.
# First game illustrates the principle of Fibonacci numbers

from abc import ABC, abstractmethod


class MathsGame(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def play_game(self):
        pass

    @property
    @abstractmethod
    def user_input_property(self):
        pass

class Fibonacci(MathsGame):
    def __init__(self):
        self.__user_input = 0
        super().__init__()

    def play_game(self):
        how_many = int(input("How many Fibonacci numbers? "))

        # Fibonacci game
        term1, term2 = 0, 1
        count = 0

        print("[", end='')

        if how_many <= 0:
            print("Please enter a number greater than 0")
        elif how_many == 1:
            print(term1)
        else:
            while count < how_many:
                print(term1, end='')
                next_term = term1 + term2
                term1 = term2
                term2 = next_term
                count += 1
                if count < how_many:
                    print(", ", end='')
        print("]")

    @property
    def user_input_property(self):
        return self.__user_input

    @user_input_property.setter
    def user_input_property(self, value):
        self.__user_input = value

f = Fibonacci()
f.play_game()