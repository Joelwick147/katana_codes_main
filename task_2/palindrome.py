#ask for input the input either sentence, word or number
sample =input("Enter a word ")

#convert the input into lower case for easy standardization and also remove space
sample = sample.lower().replace(" ", "") 

#we start reading the sample from behind using slicing or reverse function
sample_reverse =sample[ : :-1]

#compare the letters to see if they are the same 
if sample ==sample_reverse:
    print("This is a palindrome")
else:
    print("This is not a palindrome")

