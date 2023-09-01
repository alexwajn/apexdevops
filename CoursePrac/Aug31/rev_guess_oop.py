import random

class ReverseGuessingGame:
    MAX_NUM = 100
    MIN_NUM = 1
    n_tries = 0

    def _gen_guess(self, min, max):
        guess = random.randint(min, max)
        print(f"Is it {guess}?")
        return guess        

    def _check_guess(self):
        check = input().lower()
        return check
    
    def game_loop(self):
        try_again = True
        min_v = self.MIN_NUM
        max_v = self.MAX_NUM
        print("Type L if too low, H if too high or C if it's correct!")
        while try_again:
            guess = self._gen_guess(min_v, max_v)
            check = self._check_guess()
            if check == "l": min_v = guess + 1
            elif check == "h": max_v = guess - 1
            else: 
                try_again = False
                print("Correct!")            
            self.n_tries += 1
        print(f"I took {self.n_tries} tries to get it!")

inp = "p"
while inp == "p":
    game = ReverseGuessingGame()
    game.game_loop()
    inp = input("Press p to play again or any other character to exit:_")
print("Exiting....")


        





