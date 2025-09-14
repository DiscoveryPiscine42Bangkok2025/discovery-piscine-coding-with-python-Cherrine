def main(words):
    if not words:
        print("none")
    else:
        for word in reversed(words):
            print(word)

main(input().split())