
# There are various default variable types predefined in python.
# Some examples are:

an_integer = 5
print(type(an_integer))

a_float = 2.3
print(type(a_float))

a_string = "Hello World"
print(type(a_string))

a_boolean = True
print(type(a_boolean))

a_list = [5, 4, 2.3, "hi", False]
print(type(a_list))
print('The second element in "a_list" is:', a_list[2])

a_dictionary = {'key': 'value', 'a': 1, 'b': 2, 3: 'c', 4: 'd'}
print(type(a_dictionary))
print('The value stored in "a_dictionary" under the key "a" is:', a_dictionary['a'])
print('The value stored in "a_dictionary" under the key 4 is:', a_dictionary[4])

# Python has the usual loops and conditions:
k = 4
while k>=0:
    print(k)
    k = k-1

for k in range(9):
    if k<3:
        print('<3')
    elif k<6:
        print(k)
    else:
        print('>=6')

# you can loop over elements in a list
for element in a_list:
    print(element)

# the non-pythonic way to achieve this might look like:
for index in range(len(a_list)):
    print(a_list[index])

# here we use enumerate to also get the index
for index, element in enumerate(a_list):
    print('element number {} equals: {}'.format(index, element))  # en example of string formatting

# you can loop over the keys of a dictionary:
for key in a_dictionary:
    print(key, a_dictionary[key])

# or get the key and value in one go:
for key, value in a_dictionary.items():
    print(key, value)

# We can define functions:
def some_function(mandatory_argument, optional_argument='default_value'):
    print(mandatory_argument, optional_argument)

def cube(v):
    return v**3

# And "call" them:
some_function('hello', 'world')
some_function('hello')
print(cube(5))

# Here we define a python class.
# You might think of a class as a (potentially) very complex variable type, 
# that has it's own variables and functions inside.
class MyClassName:
    def __init__(self, input_in_init):
        # Functions inside a class are called "methods" and their first input
        # argument is always 'self'.
        # When calling the method you omit passing that argument.

        print("The special __init__ method/function is executed at the moment of instantiation")
        # Variables that are preceded by "self." can be accessed from anywhere
        # inside the object
        self.hello = "Hello World"
        self.attribute = input_in_init
        # Other variables are local to this
        some_local_variable = 7

    def some_method(self, v):
        """
        Prints a message and returns input + 10

        :param v: a number
        :type v: int or float
        :return:
        :rtype: int or float
        """
        print(self.hello)
        print(self.attribute)
        v = v+ 10
        print(v)

    def this_method_will_cause_an_error(self, input):
        # input is a variable local to this function
        print(input)
        # some_local_variable was local to the __init__ method and can't be accessed here:
        print(some_local_variable)

# Now that the MyClassName class has been defined we can create (instantiate) 
# objects of this class ("type")

a = MyClassName('aaa')  # This is not a function, but the instantiation
print(type(a))

# We can make multiple objects of the same class
b = MyClassName('bbb')
print(type(b))

# We can access "variables" of the object:
print("a.hello =", a.hello)

# We can call the methods of the object:
a.some_method(5)

# This line would cause an error, as explained in the comments inside the definition of the error:
# a.this_method_will_cause_an_error(6)

if __name__ == '__main__':
    print("Executing this code because this file was run directly instead of being imported")
    # If you were to import this module (= python file), this section of code
    # would not be executed.
    # Only if you run this file directly, this code is executed.
    # When you have multiple files (modules), it is useful to place function
    # and class definitions in the main section of the code. And use this
    # section for testing those classed or functions (mostly while developing)

