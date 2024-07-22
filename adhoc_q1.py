def func(nums):
    d = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six'} # step 2: assigning dict values to variable d
    
    numbers = [] # step 3: creating a empty list named numbers
    
    keys = [k for k in d.keys()] # step 4: collecting the keys from d variable 

    # and storing it in "keys" variable using list comprehension

    for x in range(len(nums)): # step 5: iterating through len of nums which is 6=> range(6) =>0,5
        # x=0 first iterating elemnt
        if isinstance(nums[x],str): # step 6: check if nums[0] == string then True
            numbers.append([d[x+1],keys[x]]) # step 7: Appending [d[1],keys[0]] => appending ['one',1]
        else:
            numbers.append([nums[x],d[x+1]])

    return numbers

print(func(['one',2,3,'four',5,'six'])) # step 1: calling the function