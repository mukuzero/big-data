import re

a = ['Raja Raman','Belvina,Shyamantha','Meenashree']

def character_count(word):
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

def split_string(list):

    new_list = [item for i in a for item in re.split(r"\s|,", i)]
    return new_list

split_list = split_string(a)

char_count_dict = { i: character_count(i) for i in split_list}

lookup = {1:"one",2:"two",3:"three",4:"four"}

for p_key,p_value in char_count_dict.items():
     
     for c_key,c_value in p_value.items():
            if c_value>1:
                print(f"{p_key} has {lookup[c_value]} duplicated element which is '{c_key}'")
            
