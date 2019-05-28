strings = []
def permute(string):
    for c in string:
        print(c)
        strings.append(c+permute(string.replace(c,"")))

if __name__ == "__main__":
    print(permute("abcd"))