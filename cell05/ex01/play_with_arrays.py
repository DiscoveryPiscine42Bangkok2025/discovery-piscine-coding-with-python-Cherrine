def main(array_input):
    array = [int(x.strip()) for x in array_input.strip('[]').split(',')]
    new_array = [x + 2 for x in array]
    print("Original array:", array)
    print("New array:", new_array)

main(input())