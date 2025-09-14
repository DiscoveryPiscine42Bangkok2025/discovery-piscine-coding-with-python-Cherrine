def greetings_for_all(name):
    if name:
        print(f"Hello, {name}.")
    if not name:
        print("Hello, noble stranger.")
    else:
        print("Error! It was not a name.")

greetings_for_all(input())