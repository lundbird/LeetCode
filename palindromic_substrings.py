def countSubstrings(s):
    count = 0
    for i in range(1, len(s)+1):
        for j in range(len(s)-i+1):
            substr = s[j:j+i]
            revstr = substr[::-1]
            # print(substr,revstr)
            if substr == revstr:
                count += 1
    return count


if __name__ == "__main__":
    print(countSubstrings("abc"))
    print(countSubstrings("aaa"))
