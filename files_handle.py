f = open("test.txt", "a")
f.write("\nThis text will be appended the original text")

f = open("test.txt", "r")
print(f.read())

import pandas as pd
file = pd.ExcelFile("original.xlsx")
print(file.sheet_names)

sheet = file.parse('original')
