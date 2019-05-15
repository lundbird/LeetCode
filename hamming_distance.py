def hammingDistance(x: int, y: int) -> int:
    return bin(x^y).count("1")



if __name__=="__main__":
    assert(hammingDistance(4,2)==2)
    assert(hammingDistance(1,8)==2)
    assert(hammingDistance(4,4)==0)
    assert(hammingDistance(1,3)==1)
    assert(hammingDistance(15,0)==4)
    assert(hammingDistance(15,3)==2)
