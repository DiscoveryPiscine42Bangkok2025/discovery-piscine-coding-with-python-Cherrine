def main(text):

    if len(text) == 0:
        print("none")
        return
    
    else:
        for arg in text:
            if arg.endswith("ism"):
                print(arg)
            else:
                print(arg + "ism")

main(input().split() if input else [])