"""Generates funny names y randomly combining names from 2 separate lists."""
import sys
import random


def main():
    """Choose names at random from 2 tuples of names and prints to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News')

    last = ('Appleyard', 'Bigmeat')

    while True:
        first_name = random.choice(first)

        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
