def main(number):
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

main(float(input("Give me a number: ")))