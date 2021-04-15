str1 = "deePali"

def countSmallCapital(str1):
    ex=""
    ex1=""
    count =0
    count1 =0
    for i in str1:
        if i >='a' and i<='z':
            ex += chr(ord(i)-32)
            count+=1
        elif i >='A' and i<='Z':
            ex1 += chr(ord(i)+32)
            count1+=1

    print("Small letters are ", count)
    print("Capital letters are ", count1)
   
###driver code####
makeUpper(str1)

######################################################