from animal_web_generator_services import load_animals_data, load_animals_template, serialize_animal


    
def main():
    animals_data = load_animals_data()
    template = load_animals_template()
    if animals_data and template:
        output = ""
        for animal in animals_data:
            output += serialize_animal(animal)
        
        new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)
        
        with open("animals.html", "w") as file:
            file.write(new_html)
        
        print("HTML file generated successfully with animal information.")
    else:
        print("Failed to generate HTML file due to missing data or template.")
        
if __name__ == "__main__":
    main()   

    