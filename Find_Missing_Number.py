def findMissingNumber(input):
    input.sort()
    start = input[0]
    last =input[-1]
    temp=[]
    for i in range(start,last):
        temp.append(i)
    temp.append(last)
    #print(temp)
    count = 0
    temp1=[]
    for i in temp:
        if i not in input:
            count+=1
            temp1.append(i)
    return count , temp1


input =[2,3,5,7,8,0]
print(findMissingNumber(input))
