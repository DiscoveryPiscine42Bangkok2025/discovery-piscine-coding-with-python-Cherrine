def main(args):
    
    if len(args) == 0:
        print("parameters: none")
    else:
        print(f"parameters: {len(args)}")
    
    for arg in args:
        print(f"{arg}: {len(arg)}")

main(input().split() if input else [])