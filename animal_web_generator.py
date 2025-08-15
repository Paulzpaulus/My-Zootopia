import json 

with open("animals_data.json", "r") as data:
    animals_data = json.load(data) 
    

with open("animals_template.html", "r") as template_file:
    template = template_file.read() 

output = ""
for animal in animals_data:
    name = animal.get('name')
    diet = (animal.get('characteristics') or {}).get('diet', 'Unknown')
    type_ = (animal.get('characteristics') or {}).get('type', 'Unknown')
    locs = animal.get('locations') or []
    location = locs[0] if locs else 'Unknown'
    
    output += "<li class='cards__item'>'"
    output += f"<div class='card__title'>{name}</div>\n"
    output += "  <p class='card__text'>\n"
    output += f" <strong>Diet:</strong> {diet}<br/>\n"
    output += f"      <strong>Location:</strong> {location}<br/>\n"
    output += f"      <strong>Type:</strong> {type_}<br/>\n"
    output += "  </p>\n"
    output += "</li>\n"
    
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output) 

with open("animals.html", "w") as file:
    file.write(new_html) 
    
print("HTML file generated successfully with animal information.") 

