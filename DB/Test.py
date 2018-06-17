
import pandas as pd

data = pd.read_csv('/Users/OliverWeisfeld/Desktop/code/Practise1.csv')
print(data[2:5]['AGE'])
print(data.loc[[1,3,5],['LAST_NAME','DEGREE']])