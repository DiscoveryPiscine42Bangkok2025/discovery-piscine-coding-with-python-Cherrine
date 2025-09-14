def main(first_num, second_num):
    result = first_num * second_num

    print(first_num, "x", second_num, "=", result )
    if result < 0:
        print("The result is negative.")
    elif result > 0:
        print("The result is positive.")
    else:
        print("The result is positive and negative.")

main(int(input("Enter the first number: ")), int(input("Enter the second number: ")))