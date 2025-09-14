def array_of_names():

    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    result = [f"{first.capitalize()} {last.capitalize()}" for first, last in persons.items()]
    print(result)

array_of_names()