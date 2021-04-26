"""Turn a word into its Pig Latin equivalent."""
import sys

VOWELS = 'aeiouy'


def main():
    while True:
        word = input("Type a word and get its pig Latin translation: ")

        if word[0] in VOWELS:
            pig_latin = word + 'way'
        else:
            pig_latin = word[1:] + word[0] + 'ay'
        print()
        print("{}".format(pig_latin), file=sys.stderr)

        try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
        if try_again.lower() == "n":
            sys.exit()


if __name__ == "__main__":
    main()
