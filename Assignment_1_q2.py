import re

a = ['Raja Raman','Belvina,Shyamantha','Meenashree']

def remove_duplicates(word):
        # Dictionary to store the frequency of each character
        char_count = {}
        
        # Iterate through each character in the word
        for char in word:
            # Increment the count for this character in the dictionary
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        filtered_list = [ k for k, v in char_count.items() if v == 1]
        
        filtered_list="".join(filtered_list)
        return filtered_list

def split_string(list):

    new_list = [item.lower() for i in a for item in re.split(r"\s|,", i)]
    return new_list

split_list =split_string(a)

char_count_list = [ remove_duplicates(i) for i in split_list]

print(char_count_list)