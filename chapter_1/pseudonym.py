"""Generates funny names buy randomly combining names from 3 separate lists."""
import sys
import random


def main():
    """Choose names at random from 2 tuples of names and prints to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ( "Bill", "Bob", "Bud", 'Chad', 'Chesterfield',
            'Chewy', 'Chigger', 'Cleet', 'Dennis', 'Dicman', 'Elphonso',
            'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim',
            'Huggy', 'Ignatious', 'Jimbo', "Joe", 'Johnny',
            'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
            '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
            'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
            'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
            "Sid", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
            'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
            'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
            "Winston", 'Worms', 'Mergatroid', 'Huckleberry')

    middle = ('Stinkbug', 'Beenie-Weenie', 'Pottin Soil', 'The Squirts',
            'Jazz Hands', 'Baby Oil', 'Bad News', 'Big Burps', 'Lite',
            'Butterbean', 'Buttermilk', 'Buttocks', 'Bowel Noises', 
            'Boxelder', 'Cinnabuns', 'Cornbread', 'Crab Meat',
            'Crapps', ' Clawhammer', 'Dark Skies',)

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderso n',
            'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee',
            "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
            'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
            'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
            'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
            'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
            'Wimplesnatch', 'Winterkorn', 'Woolysocks')

    while True:

        first_name = random.choice(first)

        middle_name = random.choice(middle)

        last_name = random.choice(last)

        print("\n\n")
        print("{} {} {}".format(first_name, middle_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
