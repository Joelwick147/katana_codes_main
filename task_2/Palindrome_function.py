#Palindrome Checker
import string
 
def reversed_sample(text):
    return''.join(reversed(text))

#remove spaces and turn any phrase into lower case

def un_reversed_sample(text):
    return ''.join(char.lower() for char in text if char.isalnum())

def is_palindrome(text):
    clean_sample=un_reversed_sample(text)
    return clean_sample == reversed_sample(clean_sample)
    
#user input
user_input =input("Enter any word or phrase:  ")

#show the results after checking
if is_palindrome(user_input):
    print("it's a palindrome")
else:
    print("It's not a palindrome")