from random import randint
from tkinter import *
from tkinter import messagebox
from functools import wraps

window = Tk()


class GuessingGame:
    upper_bound = 100
    lower_bound = 1
    count = 1

    def __init__(self,num=input("Choose your number between 1 and 100: ")):

        while True:
            try:
                self.num = int(num)
                break

            except ValueError:
                print("Must be an integer between 1-100")
                num = input("Choose your number between 1 and 100: ")

        self.computer_choice = None

    def main(self):
        self.computer_choice = randint(GuessingGame.lower_bound,GuessingGame.upper_bound)

        while self.computer_choice:
            print(f"Computer chose {self.computer_choice}")

            if self.computer_choice > self.num:
                self.too_high()

            elif self.computer_choice < self.num:
                self.too_low()

            elif self.computer_choice == self.num:
                self.correct()

            GuessingGame.count += 1
            self.main()

    def correct(self):
        print(f"It took {GuessingGame.count} tries to hit the number")
        exit()

    def too_low(self):
        GuessingGame.lower_bound = self.computer_choice + 1

    def too_high(self):
        GuessingGame.upper_bound = self.computer_choice - 1


if __name__ == '__main__':
    game1 = GuessingGame()                                   # Initialize a guessing game. And give our starting number
    game1.main()                                             # Start the game

    while True:
        if messagebox.askyesno(title="Play Game?", message="Do you want to play again?"):
            game = GuessingGame()
            game.main()
        else:
            print("You've exited the game")
            break


