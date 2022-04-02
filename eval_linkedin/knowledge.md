# Knowledge

## Respond to question of quizz

- What is the difference between class attribute and instance attribute ? 

Class attributes are the variables defined directly in the class that are shared by all objects of the class. 

Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor. 

Example : 

class Student:
    count = 0
    def __init__(self):
        Student.count += 1      



>>> std1=Student()
>>> Student.count
1
>>> std2 = Student()
>>> Student.count
2


count are a class attribute. 

- How to retrieve the keys of a dictionnary ? 

Use dict.keys(). Take care of the ().

Example : 

dict = {1:'a', 2:'b', 3:'c'}
print(dict.keys())
>>> [1, 2, 3]

- Range function  

The parameter 'stop' is never in the generated list. 

For example: 
for i in range(10):
    print(i) 
>>> [0,1,2,3,4,5,6,7,8,9]

for i in range(0,10,2):
    print(i) 
>>> [0,2,4,6,8]

for i in range(10,1,-1):
    print(i) 
>>> [10,9,8,7,6,5,4,3,2]

- What did a function if there is no return statement ? 

They return a None value

- What happened if we don't put a condition to stop a while loop ? 

There is an infinite loop

- Methods to read external files : 

With the open(path_to_file, mode) method, there is 3 principal modes to interact with files : 'w' to write in a file, 'r' to read a file and 'a' to append text to the end of a file.

## New knowledge I don't have before

- from https://docs.python.org/3/tutorial/index.html

- To ask to the user of the prompt to enter something and to retrive it, use the method input()

- Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.

- A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.

Example : 

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

- Return statement : return without an expression argument returns None.

- Zip method : 

 zip(*iterables, strict=False)

    Iterate over several iterables in parallel, producing tuples with an item from each one.

    Example:
    >>>

    >>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    ...     print(item)
    ...
    (1, 'sugar')
    (2, 'spice')
    (3, 'everything nice')

- To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

-  all(iterable)

    Return True if all elements of the iterable are true (or if the iterable is empty).

-  any(iterable)

    Return True if any element of the iterable is true.

- bin(x)

    Convert an integer number to a binary string prefixed by "0b".

- chr(i)

    Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'.

- filter(function, iterable)

Construct an iterator from those elements of iterable for which function returns true.

Example

```
# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)

Output : 
The filtered letters are:
e
e
```

- getattr(object, name)

Return the value of the named attribute of object. For example, getattr(x, 'foobar') is equivalent to x.foobar.

- map(function,iterable)

Return an iterator that applies function to every item of iterable.

- The different mode for the open() method : 
    - 'r' : open for reading (default)
    - 'w' : open for writing, truncating the file first
    - 'x' : open for exclusive creation, failing if the file already exists
    - 'a' : open for writing, appending to the end of the file if it exists
    - 'b' : binary mode 
    - 't' : text mode   
    - '+' : open for updating (reading and writing)

- The method open() return a file object

- The @property decorator turn a method into a "getter" for a read-only attribute with the same name

Example :

```
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```





- TODO: continue to explore built-in methods that I don't know






