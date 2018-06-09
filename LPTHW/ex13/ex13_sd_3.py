from sys import argv
script, age, gender, place = argv
print("The script is called:", script)
print("Your age is:", age)
print("Your gender is:", gender)
print("You live in:", place)
feeling = input("How are you feeling? ")
print("You are feeling:", feeling)

'''
Output:

$ python ex13_sd_3.py 21 Male Siliguri
The script is called: ex13_sd_3.py
Your age is: 21
Your gender is: Male
You live in: Siliguri
How are you feeling? awesome
You are feeling: awesome
'''