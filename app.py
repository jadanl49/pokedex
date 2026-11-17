import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
moves = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
moves = json.load(moves)


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

def name(x,y):
    for i in range(x,y):
        print(data[i]["name"]["english"])
""" name(0,len(data)) """


# Add a language choice feature and print the pokemons name based on the user input
def language(x,y):
    z = input("what language")
    if z.lower == ["english", "japanese", "french", "chinese"]:
        print("printing", z)
    else: 
        print("Language not found")
        return
        

    for i in range(x,y):
        print(data[i]["name"][z])
""" language(0,len(data)) """

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def typelist(x,y):
    z = input("What type of pokemon?").lower()
    matching = []
    for i in range(x,y):
        if z in [typefinder.lower() for typefinder in data[i]["type"]]:
            matching.append(data[i]["name"]["english"])
        
        if matching: 
            print("Printing all", z , "Types")
            for pokemon_names in matching:
                print(pokemon_names)

        else: 
            print("No pokemon found!")
            return
typelist(0,len(data)) 




#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

""" o = input("What is the name of the pokemon")   """
searchlist = []
def pokemonfinder(o):

    
    findcount = 0
    for i in range(len(data)):
        if o.lower() in data[i]["name"]["english"].lower():
            print(data[i]["name"]["english"])
            searchlist.append(data[i]["type"])
            findcount += 1
    if findcount > 0:
        print(f"Pokemon found: {findcount}")
    else:
        print("No pokemon were found.")
""" pokemonfinder(o)  """

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
""" o = input("Which pokemon would you like to learn about?")

def movefinder(o):
    matching_pokemon = []
    movefind = 0
    for pokemon in data:
        if o.lower() in pokemon["name"]["english"].lower():
            matching_pokemon.append(pokemon)
        if not matching_pokemon:
            print("No pokemon were found!")
            return
         

        moveset = []

        if moveset:
            print(f"Moves found for {o}:")
        
    if movefind > 1:
        print(f"Moves found: {moveset}")
    else:
        print("No moves were found!")
movefinder(o)

 """