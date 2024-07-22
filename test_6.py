import pandas as pd
a=5

try:
    # Your code here, for example:
    result = 10 / 0  # This will raise a ZeroDivisionError
except pd.errors.EmptyDataError as ede_error:
    print(f"No data: {ede_error}")
print(a)

