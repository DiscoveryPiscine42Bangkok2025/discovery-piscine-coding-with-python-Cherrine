def main(args):
    if not args:
        print("Numbers of parameters: 0")
        return
    else:
        count = len([arg for arg in args])
        print("Numbers of parameters:", count)

main(input().split() if input else [])