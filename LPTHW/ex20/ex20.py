from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind kind of like a tap.")
rewind(current_file)

print("Let's print three lines:")

current_line  = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


'''
Output:

$ python ex20.py file_1.txt
First let's print the whole file:

Here's a new file.
Adding dummy line.
Just typing anything possible.
So now we have 4 lines.

Now let's rewind kind of like a tap.
Let's print three lines:
1 Here's a new file.

2 Adding dummy line.

3 Just typing anything possible.
'''