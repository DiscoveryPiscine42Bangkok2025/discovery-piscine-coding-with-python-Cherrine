def shrink(text):
    return text[:8]

def enlarge(text):
    return text + ('Z' * (8 - len(text)))

def methods_everywhere(args):
    if not args:
        print("none")
        return
    
    for text in args:
        if text:
            if len(text) > 8:
                result = shrink(text)
            elif len(text) < 8:
                result = enlarge(text)
            else:
                result = text
            print(result)

args = input().split()
methods_everywhere(args)