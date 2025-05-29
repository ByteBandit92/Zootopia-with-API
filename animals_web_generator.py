import data_fetcher

def generate_html(animal_name, animals):
    """
    Generates an HTML file from a template, injecting animal data.

    Parameters:
    - animal_name (str): The name of the animal being searched.
    - animals (list): A list of dictionaries, each containing details about a matching animal.
    """
    try:
        with open("animals_template.html", "r", encoding="utf-8") as template_file:
            template = template_file.read()

        if not animals:
            animals_html = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
        else:
            animals_html = ""
            for animal in animals:
                animals_html += f"<h2>{animal['name']}</h2>\n<ul>\n"
                taxonomy = animal.get("taxonomy", {})
                for key, value in taxonomy.items():
                    animals_html += f"<li><strong>{key.title()}</strong>: {value}</li>\n"
                animals_html += "</ul>\n"

                characteristics = animal.get("characteristics", {})
                animals_html += "<p><strong>Interesting Facts:</strong></p>\n<ul>\n"
                for key in ["slogan", "diet", "top_speed", "lifespan", "habitat"]:
                    if key in characteristics:
                        label = key.replace("_", " ").title()
                        animals_html += f"<li>{label}: {characteristics[key]}</li>\n"
                animals_html += "</ul>\n"

        final_html = template.replace("__REPLACE_QUERY__", animal_name)
        final_html = final_html.replace("__REPLACE_ANIMALS_INFO__", animals_html)

        with open("animals.html", "w", encoding="utf-8") as output_file:
            output_file.write(final_html)

        print("Website was successfully generated to the file animals.html.")
    except FileNotFoundError:
        print("Error: Template file 'animals_template.html' not found.")



def main():
    animal_name = input("Enter a name of an animal: ").strip()
    animals = data_fetcher.fetch_data(animal_name)
    generate_html(animal_name, animals)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()