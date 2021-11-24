#functions that dont need names
#functions that take other functions as args
a_squre = lambda x : x**2 #Single param
print(a_squre(9)) 

#Double params


"""map() is a higher-order built-in 
function that takes a function and iterable as inputs, and returns an iterator that applies the function 
to each element of the iterable. The code below uses map() to find the mean of each list in numbers to 
create the list averages. Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined 
within the call to map()."""
find_volume = lambda x,y,z : x * y * z
print(find_volume(9,2,10))


numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

# Quiz: Lambda with Filter
# Rewrite this code to be more concise by replacing the is_short function with
# a lambda expression defined within the call to filter()

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)


# With lambda
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda city: len(city) < 10, cities))

print(short_cities)


#GENERATORS VS ITERATORS
#Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in
# memory, or when the cost to calculate each list element is high 
# and you want to do it as late as possible. But they can only be iterated over once.
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
print(my_range) #Outputs the iterator object

#To print the items in the iterator my_range
it_list = []
for i in my_range(9):
    it_list.append(i)

print(it_list)

#Implement my_enumerate
#Write your own generator function that works like the built-in function enumerate.
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    i = start
    for num in iterable:
        yield i, num
        i += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


"""Chunker
If you have an iterable that is too large to fit in memory in full (e.g., 
when dealing with large files), being able to take and use chunks of it 
at a time can be very valuable."""


def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))

#Generator Expressions
# Here's a cool concept that combines generators and list comprehensions! You can actually create a 
# generator in the same way you'd normally write a 
# list comprehension, except with parentheses instead of square brackets. 
# For example:
sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

sq_iterator_items = []
for i in sq_iterator:
    sq_iterator_items.append(i)

print(sq_iterator_items)