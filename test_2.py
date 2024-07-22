variable_list = [1,2,3,4]



def return_element(list):    
    for element in variable_list:
        yield element

print(type(return_element(variable_list)))

print(return_element(variable_list))
