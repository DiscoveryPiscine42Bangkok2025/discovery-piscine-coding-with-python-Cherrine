def main(keywords, text):

    count = 0

    if not keywords or not text:
        print("none")
    else:
        for word in text.split():
            if keywords.lower() in word.lower():
                count += 1

    print(count)

main(input(), input())