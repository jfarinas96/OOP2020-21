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
        pass

    @property
    def user_input_property(self):
        return self.__user_input

    @user_input_property.setter
    def user_input_property(self, value):
        self.__user_input = value
