# from the module sys, import the function or parameter argv
from sys import argv
# Get the filename
script, filename = argv
# Open the file
txt = open(filename)
# Normal print statement
print(f"Here's your file {filename}:")
# print content of file
print(txt.read())
# Ask for a new file name or user may type the same filename again
print("Type the filename again:")
file_again = input("> ")
# open the file
txt_again = open(file_again)
# display file contents again
print(txt_again.read())


'''
Output:

$ python ex15.py test_1.txt
Here's your file test_1.txt:
Hey this is the first file.
It just contains few random words.
I like Machine Learning
Hope we learn new thing everyday.

Type the filename again:
> test_2.txt
Good Evening everyone.
We have a nice whether today.
visit r/MachineLearning and r/programming daily if you want to keep yourself updated.
Goodbye.
'''