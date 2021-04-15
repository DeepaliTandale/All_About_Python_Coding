def reverse_number(n):
    final_string = ""
     
    n =str(n)
    if n[0] == '-':
        final_string+=n[0]
    n =n[1:]
    
    for i in n[::-1]:
        final_string+=i

    #print(final_string)

    return final_string

    
n = -123
print(reverse_number(n))