import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


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

#    for i in range(x,y):
  #    if z.lower() in data[i]["type"]:
 #           print(data[i]["name"]["english"]) 
    
    
    for z in ["type"] in data:
        print("Printing All", z, "Types")
    else:
        print("Thats not a type")
        return
typelist(0,len(data))






#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

""" o = input("What is the name of the pokemon") """
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
""" pokemonfinder(o) """

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!