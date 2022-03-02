
# in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module
from functools import reduce

#! REDUCE ---> ONE VALUE FROM ALL
#! reduces effort

#! SYNTAX : reduce(function, sequence[, initial])

#? unlike map and reduce function which return a new list based on the function and iterable we've passed.
#? reduce function returns a single value computed

list2 = ["abc", "klm", "def"]
maxl = reduce(lambda a, b:a if a>b else b, list2)
print(maxl)

# TODO : PRINT THE OUTPUT OF THE FOLLOWING OPERATIONS USING INPUT FROM A LIST
mul = (1,2,3,4,5)
s1 = reduce(lambda a, b : a * b, mul)
s2 = reduce(lambda a, b : a + b, mul)

print('Sum of list1 :', s1)
print('Sum of list1 :', s2)

# TODO : PRINT THE OUTPUT OF THE FOLLOWING OPERATIONS USING INPUT FROM THE USER

numbers = (input("Enter : "))
number1 = numbers.split(",")
op1 = list(map(int,number1))
op2 = reduce(lambda a,b : a*b , op1)
op3 = reduce(lambda a,b : a+b , op1)
print("The multiplication of the numbers is ",op2)
print("The addition of the numbers is ",op3)

# TODO : Custom reduce function in python

def reduceIt(func,sequence) :
    res=sequence[0]
    for variable in sequence[1:]:
        res =func(variable,res)

    return res

def addIt(a,b):
    return a+b

seq=[1,2,3,4,5]
print(str(reduceIt(addIt,seq)))
