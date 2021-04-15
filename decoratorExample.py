def decorator_example(function):
    print("in decorator")
    def interchange(a,b):
        print("a = ",a,"b =",b)
        if a<b:
            a,b = b,a
            print("a = ",a,"b =",b)
        return function(a,b)
    return interchange


@decorator_example
def divide(a,b):
    print("Output is ")
    return a//b

#divi = decorator_example(divide)
print(divide(4,16))

# def plus_one(number):
#     return number + 1

# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)

# print(function_call(plus_one))