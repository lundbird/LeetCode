def flipAndInvertImage(A):
    return [[1-i for i in row[::-1]] for row in A]

if __name__ == "__main__":
    assert flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0] == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] ,  flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]