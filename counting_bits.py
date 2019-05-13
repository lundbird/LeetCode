def countBits1(num):
    return [bin(val).count("1") for val in range(num+1)]

def countBits2(num):
    return [sum((val & (1 << i) != 0 for i in range(val))) for val in range(num+1)]
    
def countBits3(num):
    res = [0]
    while len(res) <= num:
        print([i+1 for i in res])
        res += [i+1 for i in res]
    return res[:num+1]

if __name__=="__main__":
    print(countBits1(8))