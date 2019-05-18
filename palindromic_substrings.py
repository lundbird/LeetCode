def countSubstrings(s):
    count = 0
    for i in range(2, len(s)+1):
        for j in range(len(s)-i+1):
            substr = s[j:j+i]
            if substr == substr[::-1]:
                count += 1
    return count+len(s)


if __name__ == "__main__":
    print(countSubstrings("abc"))
    print(countSubstrings("aaa"))
