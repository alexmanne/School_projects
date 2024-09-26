import random
import string

# Reads in the file of wordle words
def read_file(infile):
    with open(infile) as file:
        return file.readlines()


# Prints the response to your guess
def print_response(target, guess, remaining_letters):
    response = ""
    already_right = ""     # Helps guarantee a '?' only appears when helpful
    for c_tar, c_guess in zip(target, guess):
        if c_tar == c_guess:
            response += "!"
            already_right += c_guess
        elif c_guess in target and c_guess not in already_right:
            response += "?"
        else:
            response += "*"
            remaining_letters.remove(c_guess)
    return response


def main(infile, allowed_attempts):

    # Initial values
    list_of_words = read_file(infile)
    remaining_letters = list(string.ascii_lowercase)     # ['a', 'b', ..., 'z']
    target = random.choice(list_of_words)
    attempt = 1

    # Print pre-game sequence
    print("\nThe Wordle!")
    print("Here are the rules:")
    print("- The '*' means that letter is not in the word.")
    print("- The '?' means that letter is in the word, but in the wrong spot.")
    print("- The '!' means that letter is in the right spot!\n")

    # Play the game
    while True:

        # If they run out of attempts, break and print end-game sequence
        if attempt > allowed_attempts:
            print(f'Maybe next time. The answer is {target}.')
            break

        # Show the player their remaining letters and accepts their guess
        print("Remaining Letters: ", ", ".join(remaining_letters))
        guess = input(f"Guess # {attempt}: \n")

        # Calculate response and print it
        response = print_response(target, guess, remaining_letters)
        print(response, "\n")  

        # If they guess correctly, break and print end-game sequence    
        if guess == target.strip():
            print("Way to go!")
            break

        attempt += 1


if __name__ == '__main__':
    main("wordle-answers-alphabetical.txt", 6)
