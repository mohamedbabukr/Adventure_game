
from asyncio.windows_events import NULL
import time
import random
from xml.etree.ElementTree import TreeBuilder
monsters = ["evil chicken", "gaint ant", "bird monster"]


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option} is invalid. Try again!')


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(monster):
    print_pause("you find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"rumor has it that a {monster} is  "
                "around and has been terrifying the nearby village.")
    print_pause("there is a house infront of you,"
                " and to the"" right is a dark cave")
    print_pause("And you have your trusty "
                "(but no very effective) dagger.")


def field(items, monster):
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to explore the cave.\n"
                "what whould you like to do?")

    response = valid_input("(Please enter 1 or 2).\n", ['1', '2'])
    if response == '1':
        house(items, monster)
    elif response == '2':
        cave(items, monster)
    else:
        print_pause("(Please enter 1 or 2)")


def house(items, monster):
    print_pause("you knock on the door of the house")
    print_pause(f"only to find out its the {monster} nest")
    fight(items, monster)


def fight(items, monster):
    print_pause(f"{monster} attacks what will you do\n"
                "1 fight back\n"
                "2 run away")
    choice = valid_input("(please enter 1 or 2)\n", ['1', '2'])
    if choice == '1':
        if "long sword" in items:
            print_pause(f"you pull your long sword then the {monster} flies.\n"
                        "congrats you saved the village")
            play_again()
        else:
            print_pause("Your dagger is not effective enough you have"
                        " been defeated")
            play_again()

    elif choice == '2':
        print_pause("you have fled and you where not triled back to the "
                    "field.")
        field(items)


def play_again():
    again = valid_input("Would you like to play again \n"
                        "Enter 1 for yes\n"
                        "Enter 2 for no\n", ['1', '2'])
    if again == '1':
        play_game()
    else:
        print_pause("thanks for playing")


def cave(items, monster):
    if "long sword" in items:
        print_pause("The dark cave is emtpy there is nothing to do here")
        field(items, monster)
    else:
        print_pause("you go in the dark cave, you relize its small behind a\n"
                    " big rock you see a piece of metal shining, a long sword")
        print_pause("you pick it and place it in your inventory")
        items.append("long sword")
        print_pause("then you go back to the field")
        field(items, monster)


def play_game():
    items = []
    monster = random.choice(monsters)
    intro(monster)
    field(items, monster)


play_game()
