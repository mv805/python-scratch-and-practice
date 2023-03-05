import random


class GuessingGame:

    # attributes
    guesses = 0
    MAX_SECRET_NUMBER = 100
    MIN_SECRET_NUMBER = 1

    def __init__(self):
        secret_number = random.randint(
            self.MIN_SECRET_NUMBER, self.MAX_SECRET_NUMBER)

    def getGuesses(self):
        return self.guesses

    def takeGuess(self):
        guess = input("What is your guess?")
        if (guess > 100 or guess < 1):
            print("OUT OF BOUNDS")
        else:
            self._compareGuess(guess)

    def _compareGuess(self, guess):
        pass
    
    def _checkWin(self):
        pass
