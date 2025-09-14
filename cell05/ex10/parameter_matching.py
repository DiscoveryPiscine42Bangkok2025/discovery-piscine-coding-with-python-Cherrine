def main():
    param1 = input()
    if param1 == "":
        print("None")
        return

    param2 = input("What was the parameter? ")
    if param1 == param2:
        print("Good job!")
    else:
        print("Nope, sorry...")

main()