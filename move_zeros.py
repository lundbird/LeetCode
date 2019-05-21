def moveZeroes1(nums):
    #can modify the argument if we use [:] lol
    nums[:] = [val for val in nums if val != 0] + [0]*nums.count(0)

def moveZeroes2(nums):
    i = 0
    zero_count = nums.count(0)
    while i < (len(nums)-zero_count):
        if nums[i] == 0:
            nums.append(nums[i])
            nums.pop(i)
        else:
            i += 1

def moveZeroes3(nums):
    # brute force solution
    for i in range(0,len(nums)):
        for i in range(0,len(nums)-1):
            if nums[i] == 0:
                nums[i+1],nums[i] = nums[i],nums[i+1]

def moveZeroes4(nums):
    #doesnt work as python wont let you modify the for loop index
    zero_count = nums.count(0)
    for i in range(len(nums)-zero_count):
        if nums[i] == 0:
            nums.append(nums[i])
            nums.pop(i)
            i -=1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums)