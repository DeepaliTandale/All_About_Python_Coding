def secondOcc(input):
    temp=set()

    for i,num in enumerate(input):
        if num  in temp :
            print(num)
        else:
            temp.add(i)

    if len(temp) == len(input):
        return -1



input = [2,1,3,5,3,2]
secondOcc(input)