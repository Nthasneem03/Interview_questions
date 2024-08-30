# python program to find last word and length of last word in a string

def length_of_last_word(s):
    words = s.split()                                                   # Split the string into word
    last_word = words[-1]                                               # extract the last word 
    print('Last word of given string:',last_word)                       # print the last word 
    last_word_length = len(last_word)                                   # Extract the length of the last word
    print('Length of last word of given string:',last_word_length)      # print length of last word


""" 
call the function to any string 
example :

"""
s1 = "Hello World"
length_of_last_word(s1)  

s2 = "   fly me   to   the moon  "
length_of_last_word(s2) 

s3 = "luffy is still joyboy"
length_of_last_word(s3) 
