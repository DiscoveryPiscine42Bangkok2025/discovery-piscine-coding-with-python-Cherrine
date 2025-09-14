def main(text):
    for char in text:
        if char.islower():
            print(char.upper(), end="")
        else:
            print(char.lower(), end="")

main(input())