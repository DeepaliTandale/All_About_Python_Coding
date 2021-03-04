def TwoSum(input,target):
    temp={}
    for i,num in enumerate(input):
        if target-num in temp:
            return temp[target-num], i

        temp[num]=i

input = [2,6,8,2,0,1]
print(TwoSum(input,3))