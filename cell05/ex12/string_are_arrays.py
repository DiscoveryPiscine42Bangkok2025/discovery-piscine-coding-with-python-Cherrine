def main(text):
    char_array = list(text.lower())
    count = 0
    
    for i in range(len(char_array)):
        if char_array[i] == 'z':
            count += 1
    print(count)

main(input())