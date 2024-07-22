# Generators are a type of iterable, like lists or tuples,
# but instead of storing all their values in memory,
# they generate values on the fly. 
# Generators are useful when dealing with large datasets as they are memory-efficient.

# Generators can be used to process large data files 
# line by line without loading the entire file into memory.
# This is especially useful for big data transformations.
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

def filter_errors(lines):
    for line in lines:
        if "ERROR" not in line:
            yield line

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