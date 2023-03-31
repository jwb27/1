#
# Template for Python program
# Name: James Bond
# Date : 2023/03/27
#


import pandas as pd

# 1. Input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)
print(raw_data.info())

# 2. Process
M3nu = len(raw_data)
data = raw_data.sort_values(["Menu"],ascending=True)

# 3. Output
print(f'count:{M3nu}')
print(data)