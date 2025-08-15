import json 

with open("animals_data.json", "r") as data:
    animals_data = json.load(data) 
    

""" def get_animal_info(animals_data):
    for animal in animals_data:
        if "name" in animal:
            print(f"Name: {animal['name']}")
        if "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal:
            print(f"Locations: {animal['locations'][0]}")
        if "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")
        print()
 """



with open("animals_template.html", "r") as template_file:
    template = template_file.read() 

output = ""
for animal in animals_data:
    name = animal.get('name', 'Unknown')
    diet = (animal.get('characteristics') or {}).get('diet', 'Unknown')
    typ  = (animal.get('characteristics') or {}).get('type', 'Unknown')
    locs = animal.get('locations') or []
    location = locs[0] if locs else 'Unknown'
    
    output += f"Name: {name}\n"
    output += f"Diet: {diet}\n"
    output += f"Location: {location}\n"
    output += f"Type: {typ}\n\n"

new_html = template.replace("__REPLACE_ANIMALS_INFO__", output) 

with open("animals.html", "w") as file:
    file.write(new_html) 
    
print("HTML file generated successfully with animal information.")