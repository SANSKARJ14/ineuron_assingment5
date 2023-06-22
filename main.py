#ASSINGMENT 5
# 1. What does an empty dictionary code look like?
dictinary = { }
dictinary = dict( )

#2. What is the value of a dictionary value with the key;foo and and the value 42?
my_dict = {'foo': 42}
value = my_dict['foo']
print(value)

#3. What is the most significant distinction between a dictionary and a list?
"""
A dictionary is an unordered collection of key-value pairs. Each key in a dictionary is unique. 
List: A list is an ordered collection of elements. 

Dictionary: Dictionary elements are accessed by their keys rather than indices. 
Using a key, you can directly retrieve the corresponding value.
List elements are accessed using indices,

Dictionaries are commonly used when you want to store and retrieve values based on unique keys.
Lists are typically used when you need to maintain an ordered collection of elements. 
"""
"""
4. What happens if you try to access spam[foo] if spam is {bar: 100}?

we get key error because the key 'foo' does not exist in the dictionary spam.
"""
"""
5. If a dictionary is stored in spam, what is the difference between the expressions cat in spam and
cat in spam.keys()?

'cat' in spam checks for the presence of the key 'cat' directly in the dictionary spam, while 'cat'
in spam.keys() checks for the presence of the key by first obtaining a list of all the keys in spam 
"""
"""
6. If a dictionary is stored in spam, what is the difference between the expressions cat; 
in spam and in spam.values()?

same as answer 5 but instaed of showing keys this show values of dictinary 
"""
"""
7. What is a shortcut for the following code?
if color; not in spam:
spam[color] = black&;

A shortcut for the given code is to use the dict.setdefault() method.
It allows you to set a default value for a key in a dictionary if the key is not already present
spam.setdefault('color', 'black')
"""
"""
8.How do you pretty print; dictionary values using which module and function?
import pprint
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
pprint.pprint(my_dict)
"""