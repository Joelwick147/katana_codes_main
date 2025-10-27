def count_vowels(sentence):
    #convert any case letter to lower case
    sentence =sentence.lower()
    vowels =["a","e","i","o","u"]
    counts ={vowel:0 for vowel in vowels}
    total_vowels=0
    
    for char in sentence:
        if char in vowels:
            counts[char] += 1
            total_vowels +=1
#print the total number of vowels        
    print(f"{total_vowels} vowels found")
    return counts

sentence =input("Enter a sentence : ")
vowel_counts =count_vowels(sentence)

for vowel, count in vowel_counts.items():
    print(f"{vowel}:{count}")
