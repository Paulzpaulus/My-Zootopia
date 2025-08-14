import json 

with open("animals_data.json", "r") as data:
    animals_data = json.load(data) 
    
    
    
    
        
#print(type(animals_data))                 # list 
#print(len(animals_data))                  # 19
#first = animals_data[0]                   
#print(type(first), first.keys())          # dict, dict_keys(['name', 'taxonomy', 'locations', 'characteristics'])
#print(first["characteristics"].keys())    # dict_keys(['distinctive_feature', 'temperament', 'training', 'diet', 'average_litter_size', 
#                                            'type', 'common_name', 'slogan', 'group', 'color', 'skin_type', 'lifespan'])
#print(first["locations"][:3])             # list 

def get_animal_info(animals_data):
    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal:
            print(f"Locations: {animal["locations"][0]}")
        if "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")
    
        print()

get_animal_info(animals_data)

