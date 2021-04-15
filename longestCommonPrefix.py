def longestCommonPrefix(strs):
    temp = []
    if strs:
        for l,i in enumerate(strs[0]):
            if i == strs[-1][l]:
                temp.append(i)
            else:
                break
            
        return ''.join(temp)
    else:
        return ""



strs = ["flower","flow","ight"]
print(longestCommonPrefix(strs))