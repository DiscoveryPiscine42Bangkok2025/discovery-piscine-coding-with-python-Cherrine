def main(text):
    text = text.strip()

    if not text:
        print("none")
        return

    if text.startswith('"'):
        end_quote = text.find('"', 1)
        if end_quote != -1:
            result = text[1:end_quote]
        else:
            result = ""
    else:
        result = text.split()[0]

    print(result)


main(input())
