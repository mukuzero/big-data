# What is list comphrension?

# Code Assignments:
import re
# https://pynative.com/python-regex-split/#h-regex-example-to-split-a-string-into-words
a = ['Raja Raman','Belvina,Shyamantha','Meenashree']
# t=re.split(r"\s|,",a[1])
# t=[]
# for i in a:
#     t=t+re.split(r"\s|,",i)
# print(t)
def reverse_string(list):

    new_list = [item[::-1] for i in a for item in re.split(r"\s|,", i)]
    return new_list

def remove_duplicate(list):

    new_list = [item for i in a for item in re.split(r"\s|,", i)]
    def count_duplicates(word):
        # Dictionary to store the frequency of each character
        char_count = {}
        
        # Iterate through each character in the word
        for char in word:
            # Increment the count for this character in the dictionary
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        return char_count
    t=count_duplicates('raja')
    t_new= {}
    for key,value in t.items():
        if value ==1:
            t_new[key]=value
        else:
            pass
    return t_new
    
print(remove_duplicate(a))