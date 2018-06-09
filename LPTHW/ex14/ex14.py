from sys import argv
script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

'''
Output:

python ex14.py 'Debakar Roy'
Hi Debakar Roy, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me Debakar Roy?
> yes
Where do you live Debakar Roy?
> Siliguri
What kind of computer do you have?
> High End

Alright, so you said yes about liking me.
You live in Siliguri. Not sure where that is.
And you have a High End computer. Nice.
'''