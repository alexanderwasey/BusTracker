import json

#Gets the config for the program from a file, returns as json object
def importconfig(): 
    config = {}

    configfile = open("config.txt", "r")
    configstring = configfile.read() 

    try:
        config = json.loads(configstring)
    except: 
        print("Error converting to json")
        print(configstring)

    return config
