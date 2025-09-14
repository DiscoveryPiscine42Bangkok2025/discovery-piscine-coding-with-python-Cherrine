def main(number):
    array = []
    if number >= 0:
        for i in range(0, number + 1):
            array.append(i)
    else:
        for i in range(number, 1):
            array.append(i)
    print(array)

main(int(input()))