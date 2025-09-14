def find_the_redheads():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    redheads = [name for name, hair_color in dupont_family.items() if hair_color == "red"]
    print(redheads)

find_the_redheads()