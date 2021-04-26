"""Map letters from string into dictionary & print bar chart of frequency."""
import sys
import pprint
from collections import defaultdict


def main():
    text = input("Type a short phrase: ")

    ALPHABET = 'áabcdefghijklmnopqrstuvwxyz'

    # defaultdict module lets you build dictionary keys on the fly!
    mapped = defaultdict(list)
    for character in text:
        character = character.lower()
        if character in ALPHABET:
            mapped[character].append(character)

    # pprint lets you print stacked output
    print("\nYou may need to stretch console window if text wrapping occurs.\n")
    print("text = ", end='')
    print("{}\n".format(text), file=sys.stderr)
    pprint.pprint(mapped, width=110)


if __name__ == "__main__":
    main()
