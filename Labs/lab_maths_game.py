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
    COUNTER = 0

    def __init__(self):
        self.__user_input = 0
        self.__play = 1
        self.__how_many = 0
        self.__counter = 0

    def play_game(self):
        # Loops until user enters 2 to exit program
        while True:
            # Ask user to enter 1 to play, or 2 to exit and checks that user enters an integer that is 1 or 2
            try:
                self.play_property = int(input("Enter 1 to play, or enter 2 to exit: "))
                if self.play_property != 1 and self.play_property != 2:
                    print("Invalid number - enter 1 or 2\n")
                    continue
            except ValueError:
                print("Invalid input - enter 1 or 2\n")
                continue

            # Exit program if user enters 2 and displays number of correct answers
            if self.play_property == 2:
                if self.counter_property == 0:
                    print("See you next time!")
                else:
                    print("You got {0:d} number(s) correct!".format(self.counter_property))
                break

            # Loops until program doesn't come across any errors
            while True:
                # Asks for how many terms and checks that user enters an integer
                try:
                    self.how_many_property = int(input("\nHow many Fibonacci numbers? "))
                except ValueError:
                    print("Invalid input - must enter a number")
                    continue

                # Fibonacci game
                term1, term2 = 0, 1
                count = 0

                # Checks that user enters a number greater than 0
                if self.how_many_property <= 0:
                    print("Please enter a number greater than 0")
                    continue
                else:
                    print("[", end='')
                    while count < self.how_many_property:
                        print(term1, end='')
                        next_term = term1 + term2
                        term1 = term2
                        term2 = next_term
                        count += 1
                        if count < self.how_many_property:
                            print(", ", end='')
                    print("]")

                # Asks user for next term and checks that user enters an integer
                try:
                    self.user_input_property = int(input("What is the next term? "))
                except ValueError:
                    print("Invalid input - must enter a number")
                    continue

                # Check if number entered is correct and increment counter
                if self.user_input_property == term1:
                    print("Correct!\n")
                    self.counter_property += 1
                else:
                    print("Incorrect - the next term is {0:d}\n".format(term1))

                break

    @property
    def user_input_property(self):
        return self.__user_input

    @user_input_property.setter
    def user_input_property(self, value):
        self.__user_input = value

    @property
    def play_property(self):
        return self.__play

    @play_property.setter
    def play_property(self, value):
        self.__play = value

    @property
    def how_many_property(self):
        return self.__how_many

    @how_many_property.setter
    def how_many_property(self, value):
        self.__how_many = value

    @property
    def counter_property(self):
        return self.__counter

    @counter_property.setter
    def counter_property(self, value):
        if value > self.__counter + 1:
            print("Cannot increment by more than 1 at a time")
        else:
            self.__counter = value


f = Fibonacci()
f.play_game()
