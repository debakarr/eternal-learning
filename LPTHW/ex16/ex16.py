from sys import argv
script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()

print('\n\nPrinting content of file:')
# Opening the same file to read
txt = open(filename)
print(txt.read())
txt.close()

'''
Output:

$ python ex16.py file_1.txt
We're going to erase file_1.txt.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening the file...
Truncating the file. Goodbye!
Now I'm going to ask you for three lines.
line 1: If you want something, go for it, if you think you are right.
line 2: Never underestimate anyone because you might not know the potential of the person sitting next to you.
line 3: Always help one in need, making sure that they are also helping themself and you are not the only one helping.
I'm going to write these to the file.
And finally, we close it.


Printing content of file:
If you want something, go for it, if you think you are right.
Never underestimate anyone because you might not know the potential of the person sitting next to you.
Always help one in need, making sure that they are also helping themself and you are not the only one helping.
'''