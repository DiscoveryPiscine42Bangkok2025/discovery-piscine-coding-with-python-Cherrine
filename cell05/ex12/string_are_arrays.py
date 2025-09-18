def main(text):
    char_array = list(text.lower())
    count = ''
    
    for i in range(len(char_array)):
        if char_array[i] == 'z':
            count += 'z'
    print(count)

main(input())