import random

def get_guess(correct):
    guess = int(input("Guess the number:_"))
    is_guess = True
    if guess > correct:
        print("Too high.")
    elif guess < correct:
        print("Too low.")
    else: is_guess = False
    return is_guess

def main():
    inp = 'p'
    while inp == 'p':
        guess = True
        n_guesses = 0
        game_number = random.randint(1, 100)
        # print(game_number)
        while guess:
            guess = get_guess(game_number)
            n_guesses += 1
        inp = input(f"Correct! It took you {n_guesses} tries to guess the number. Press p to play again or any other character to exit:_")
    print("Exiting...")


if __name__ == '__main__':
    main()
