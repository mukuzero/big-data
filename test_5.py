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

log_file_path = 'log_file.txt'
lines = read_large_file(log_file_path)

for line in lines:
    print(line)