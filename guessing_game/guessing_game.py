import random


class GuessingGame:
    """A guessing game"""
    # attributes
    _guesses = 0
    _win = False
    _game_result = ''
    _last_guess = None

    def __init__(self, minGuess=100, maxGuess=1):

        if maxGuess > 100:
            maxGuess = 100
        if minGuess < 100:
            minGuess = 1

        self._secret_number = random.randint(
            minGuess, maxGuess)

    def getGuesses(self):
        return self._guesses

    def getSecretNumber(self):
        return self._secret_number

    def gameIsWon(self):
        return self._win

    def submitGuess(self, guess):
        if (guess == self._secret_number):
            self._game_result = "You Win!"
            self._win = True
        else:
            if (self._guesses == 0):
                self._game_result = "Nope, try another guess"
                self._last_guess = guess
            elif (guess > self._last_guess and self._last_guess > self._secret_number):
                self._game_result = "Colder!"
            elif (guess < self._last_guess and guess < self._secret_number):
                self._game_result = "Colder!"
            elif (guess > self._last_guess and guess < self._secret_number):
                self._game_result = "Warmer!"
            elif (guess < self._last_guess and guess > self._secret_number):
                self._game_result = "Warmer!"

            self._guesses += 1
        

    def getResult(self):
        return self._game_result


def game():

    game = GuessingGame(1, 10)
    print("Game is starting...")

    while (not game.gameIsWon()):

        guess = int(input("Submit a guess: "))

        if (guess < 1 or guess > 100):
            print("Out of bounds guess, try again.")
            continue

        game.submitGuess(guess)
        print(game.getResult())

    print(f"Good job you won! It took you {game.getGuesses()} guesses to win.")


game()
# establish game

# get the guess
# check win
# return status

# after win

# confirm win and how many guesses it took
