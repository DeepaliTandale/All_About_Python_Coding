def FindingMax(input):
    max1 = input[0]
    max2 = 0

    for i in range(len(input)):
        if input[i] >=max1:
            max2 = max1
            max1=input[i]
    return max1 , max2

input = [2,8,9,4,1,3]
print(FindingMax(input))