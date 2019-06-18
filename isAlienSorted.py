def isAlienSorted(words: List[str], order: str) -> bool:
    outtab = "abcdefghijklmnopqrstuvwxyz"
    table = str.maketrans(order,outtab)
    return words==sorted(words,key=lambda x: x.translate(table))