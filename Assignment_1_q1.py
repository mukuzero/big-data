import re
# https://pynative.com/python-regex-split/#h-regex-example-to-split-a-string-into-words
a = ['Raja Raman','Belvina,Shyamantha','Meenashree']

def reverse_string(list):

    new_list = [item[::-1].lower() for i in a for item in re.split(r"\s|,", i)]
    return new_list

print(reverse_string(a))