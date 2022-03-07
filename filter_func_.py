
#? The filter() function returns an iterator where :
#? the items are filtered through a function to test if the item is accepted or not.

# !FILTER --> GIVE SPECIFIC
# ! SYNTAX : filter(function, iterable/s)

#! Return an iterator yielding those items of iterable for which function(item) is true.

#! I LIKE TO REFER FILTER FUNCTION AS AN ELIGIBILITY TESTER
  
# TODO : RETURN NUMBERS GREATER THAN 5 FROM  THE LIST
list1 = [1,2,3,4,5,6,7,8,9]

def isGreater(num) :
    return num > 5

#?  here iterator is list1 for which the filter return the items for which the function isGreator is Ture
gr_than_5 = list(filter(isGreater , list1))
print(gr_than_5)

#?  here map function returns Boolean value for all items of the list for which the conditions of the function isGreater satisfies
gr_than_5 = list(map(isGreater , list1))
print(gr_than_5)

# TODO : CONVERT TO INT
#?  here filter function returns the items of list eligible to be an int after typecasting
number = ['11' , '22' , '44']
numbers = list(filter(int , number))
print(numbers)

#?  here map function actually converts the list items into int
number = ['11' , '22' , '44']
numbers = list(map(int , number))
print(numbers)

# TODO : RETURN SQUARE
num = [1,2,3,4,5,6,7,-1,0.5]

#?  here filter func returns the items of the list for which the function conditions satisfy
square  = list(filter(lambda a:a*a , num))
print(square)

# TODO : RETURN LENGTH
def myfunc(n):
  return len(n)

x = filter(myfunc, ('apple', 'banana', 'cherry'))
print (list(x))
