
# *Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
# *Returns the specified iterator with the specified function applied to each item

# *The map() function executes a specified function for each item in an iterable. 
# *The item is sent to the function as a parameter.

# *!MAP ---> GIVE ALL , CONVERT ALL ,APPLY TO ALL
# *!Syntax : 
# *!        map(function, iterable)

# *! IMP : here map func is used to typecast the list items from str to int 
numbers = ['11' , '22' , '44']
numbers = list(map(int , numbers))
print(numbers)

# *! WITHOUT USING THE LIST FUNCTION TO RETURN AN ITERABLE MADE USING MAP FUNC , print(numbers) will give the memory address
for i in range(len(numbers)) : 
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])

# TODO : map function to print square of numbers from a list
# *? defining a function
def sq (a) :
    return a*a

num = [1,2,3,4,5,6,7]
square  = list(map(sq , num))
print(square)

# *?using lambda function
square  = list(map(lambda x : x*x , num)) # *x for whatever value taken as x
print(square)

def square(a) :
    return a*a
def cube(a) :
    return a*a*a

func = [square , cube]

for i in range(5) :
    val = list(map(lambda x:x(i) , func))
    print(val)

# TODO : Calculate the length of each word in the tuple:

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
# print(list(x))

# TODO : Make new fruits by sending two iterable objects into the function:

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'),('orange', 'lemon', 'pineapple'))
# print(list(x))
