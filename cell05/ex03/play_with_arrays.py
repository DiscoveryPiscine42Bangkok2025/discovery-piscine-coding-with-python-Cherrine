def main(array_input):
    array = [int(x.strip()) for x in array_input.strip('[]').split(',')]
    
    array_no_dupes = list(set(array))
    new_array = [x + 2 for x in array_no_dupes if x > 5]
    
    print(array)
    print(new_array)

main(input())