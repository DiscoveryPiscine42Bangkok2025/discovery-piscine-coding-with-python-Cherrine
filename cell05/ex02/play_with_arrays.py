def main(array_input):
    array = [int(x.strip()) for x in array_input.strip('[]').split(',')]
    new_array = [x + 2 for x in array if x > 5]
    print(array)
    print(new_array)

main(input())