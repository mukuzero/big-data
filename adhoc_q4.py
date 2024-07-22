# Decorators are a design pattern in Python that allows a user 
# to add new functionality to an existing object
# without modifying its structure.
# Decorators are usually called before 
# the definition of a function you want to decorate.

# Decorators can be used to add logging or 
# timing functionality to your data transformation 
# functions to monitor performance and debugging.

# Example: Adding Logging with a Decorator

import datetime as dt

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = dt.datetime.now()
        result     = func(*args, **kwargs)
        end_time   = dt.datetime.now()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@log_execution_time
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

@log_execution_time
def filter_errors(lines):
    for line in lines:
        if "ERROR" not in line:
            yield line

@log_execution_time
def transform_lines(lines):
    for line in lines:
        # Transform the line (e.g., extract useful information)
        transformed_line = line.upper()  # Example transformation
        yield transformed_line

# Usage
log_file_path = 'log_file.txt'
lines = read_large_file(log_file_path)
filtered_lines = filter_errors(lines)
transformed_lines = transform_lines(filtered_lines)

for line in transformed_lines:
    print(line)  


# In Python, *args and **kwargs are used to pass a variable number of arguments to a function.
# They are very useful in writing flexible and reusable code.

# *args
# *args allows a function to accept any number of positional arguments.
# It is typically used when you don't know how many arguments will be passed to the function.
# *args is a tuple of arguments passed to the function.

# **kwargs
# **kwargs allows a function to accept any number of keyword arguments.
# It is typically used when you don't know how many keyword arguments will be passed to the function.
# **kwargs is a dictionary of the keyword arguments passed to the function.