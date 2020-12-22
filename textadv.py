# text
# user input
# read user input and make choices
# random choices
# choices

from colorama import Fore, Back, Style 
import time
adventuring = True


coords = [0, 0]


def move(action):
    global coords
    coords = {
        action == "north": [coords[0], coords[1] + 1],
        action == "n": [coords[0], coords[1] + 1],
        action == "south": [coords[0], coords[1] - 1],
        action == "s": [coords[0], coords[1] - 1],
        action == "east": [coords[0] + 1, coords[1]],
        action == "e": [coords[0] + 1, coords[1]],
        action == "west": [coords[0] - 1, coords[1]],
        action == "w": [coords[0] - 1, coords[1]],
    }[True]


def prompt(txt):
    print(Fore.GREEN + txt + "\n")


def eat(txt):
    global adventuring
    prompt("you've eaten your pokemon and you win")
    adventuring = False


commands = {
    "north": move,
    "south": move,
    "east": move,
    "west": move,
    "n": move,
    "s": move,
    "e": move,
    "w": move,
    "eat": eat,
    # "help",
    # "attack",
    # "run",
    # "talk",
    # "look",
    # "catch",
    # "heal",
    # "eat"
}





def parse_commands(input):
    input.split()


def response(*args):
    return input(Fore.WHITE + " ".join(args) + "\n").lower().strip()


def doinstuff():
    prompt(f"You are at {str(coords)} Do something please")
    action = response()
    commands[action](action)
    



def main():
    global adventuring
    choices = {"commands": commands}
    prompt("Hi Adventurer, what's your name?")
    choices["adv"] = response()
    prompt("This is my grandson, oh, what's his name?")
    choices["rival"] = response()
    pokemons = ["Squirtle", "Bulbasaur", "Charmander"]
    prompt("Pick a Pokemon: 0=Squirtle, 1=Bulbasaur, 2=Charmander")
    pokemon_picked = False
    while not pokemon_picked:
        my_pokemon = response()
        if int(my_pokemon) in range(0, 3):
            pokemon_picked = pokemons[int(my_pokemon)]
        else:
            prompt("No that sucks")
    prompt(pokemon_picked)
    while adventuring:
        doinstuff()
        
    



if __name__ == "__main__":
    main()
