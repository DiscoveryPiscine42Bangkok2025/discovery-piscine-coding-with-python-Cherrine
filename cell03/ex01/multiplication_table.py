def main():
    print("Enter a number")
    number = int(input())

    for i in range(0, 10):
        print(i, "x", number, "=", number * i)
main()