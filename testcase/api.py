# import os
#
# import openpyxl
#
#
path = r"C:\Users\Administrator\Desktop\ugot_aigc\ugot_aigc\testcase\test.xlsx"
#
#
# wb = openpyxl.load_workbook(filename=path)
# print(wb.sheetnames)

import pandas as pd

df = pd.read_excel(path, engine='openpyxl')
print(df)