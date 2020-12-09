import json

from linkedlist import LinkedList
from pokemon import *

class Pokedex(object):

        def __init__(self):
            pass

        def run(self):
            try:
                poke_list = LinkedList()
                with open("pokedex.json", "r") as file:
                    data = json.load(file)

                # Parse JSON data into a linked list of pokemon objects
                for poke in data:
                    
                    pokemon = Pokemon(poke['id'], poke['name'], poke['types'], poke['evolves_into'])
                    poke_list.add(pokemon)

                print("Pokedex Encyclopedia")
                print("1: Search by ID")
                print("2: Search by name")
                print("3: Search by type")
                print("0: Exit")
                while True:
                    user_input = input("Enter: ")
                    try:
                        user_input = int(user_input)

                        # Exit
                        if user_input == 0:
                            break;
                        
                        # Search by ID
                        elif user_input == 1:
                            id_input = input("Enter ID to search for: ")
                            if int(id_input) <= 0 or int(id_input) > poke_list.size:
                                print("ID not found\n")
                            else:
                                try:
                                    id_input = int(id_input)
                                    print(poke_list[id_input - 1])
                                except ValueError:
                                    print("ID not an integer\n")

                        # Search by name
                        elif user_input == 2:
                            name_input = input("Enter name to search for: ")
                            name_found = False
                            for members in poke_list:
                                if members.name.lower() == name_input.lower():
                                    print(members)
                                    name_found = True
                            if name_found == False:
                                print("Name not found\n")

                        # Search by type
                        elif user_input == 3:
                            type_input = input("Enter type to search for: ")
                            type_found = False
                            for members in poke_list:
                                for type in members.types:
                                    if type == type_input.lower():
                                        print(members)
                                        type_found = True
                            if type_found == False:
                                    print("Type not found\n")


                        # Invalid input
                        else:
                            print("Please choose a valid number\n")

                        print("1: Search by ID")
                        print("2: Search by name")
                        print("3: Search by type")
                        print("0: Exit")

                    except ValueError:
                        print("Please enter a number\n")
                        print("1: Search by ID")
                        print("2: Search by name")
                        print("3: Search by type")
                        print("0: Exit")

            except IOError:
                print("Error: pokedex.json file does not exist.\n")
                return


if __name__ == "__main__":
    Pokedex().run()
