def main(age):
    print(f"You are currently {age} years old.")

    for years in [10, 20, 30]:
        print(f"In {years} years you'll be {age + years} years old.")

main(int(input("Please tell me your age: ")))