def numJewelsInStones(J: str, S: str) -> int:
    return sum([S.count(val) for val in J])

if __name__=="__main__":
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J,S))


