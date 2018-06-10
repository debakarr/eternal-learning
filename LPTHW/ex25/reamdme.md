Python 3.6.4 |Anaconda custom (64-bit)| (default, Dec 21 2017, 21:42:08) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> help(ex25)
Help on module ex25:

NAME
    ex25

FUNCTIONS
    break_words(stuff)
        This function will break up words for us.
    
    print_first_and_last(sentence)
        Prints the first and last words of the sentence.
    
    print_first_and_last_sorted(sentence)
        Sorts the words then prints the first and last one.
    
    print_first_word(words)
        Prints the first word after popping it off.
    
    print_last_word(words)
        Prints the last word after popping it off.
    
    sort_sentence(sentence)
        Takes in a full sentence and returns the sorted words.
    
    sort_words(words)
        Sorts the words.

FILE
    /home/baka/Project/eternal-Learning/LPTHW/ex25/ex25.py


===============================================================================================================================================

Python 3.6.4 |Anaconda custom (64-bit)| (default, Dec 21 2017, 21:42:08) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from ex25 import *
>>> sentence = "All good things come to those who wait."
>>> words = break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> print_last_word(words)
wait.
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who']
>>> print_first_word(sorted_words)
All
>>> print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> print_first_and_last(sentence)
All
wait.
>>> print_first_and_last_sorted(sentence)
All
who
