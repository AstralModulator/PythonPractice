import pandas as pd

pd.DataFrame({'Bob':['I liked it','It was awful'],'Sue':['Pretty good','Bland']},index = ['Product A','Product B'])
pd.Series([1,2,3,4,5])

pd.Series([1,2,3,4,5],index=['Product A','Product B','Product C','Product D','Product F'],name = "Product E")