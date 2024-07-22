variable_list = [1,2,3,4]

storing_list = []

def return_element(list):    
    for element in variable_list:
        storing_list.append(element)
    return storing_list

print(return_element(variable_list))
print(type(return_element(variable_list))) 
