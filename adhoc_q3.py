def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

def filter_errors(lines):
    for line in lines:
        if "ERROR" not in line: # True if no error exists in the line
            yield line

def transform_lines(lines):
    for line in lines:
        # Transform the line (e.g., extract useful information)
        transformed_line = line.upper()  # Example transformation
        yield transformed_line

# Usage
log_file_path = '/home/mukunthan/Documents/Personal/Learning/BigData/log_file.txt'
lines = read_large_file(log_file_path) # Extract
filtered_lines = filter_errors(lines)  # Quality check
transformed_lines = transform_lines(filtered_lines) # Transform

for line in transformed_lines:
    print(line)  
# print(*transformed_lines)