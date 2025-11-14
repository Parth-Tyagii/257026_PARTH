# PANDAS 
# import pandas as pd
# data={
#     'Name':['Alice','Bob','Charlie','David'],
#     'Age':[24,27,22,32],
#     'City':['New York','Los Angeles','Chicago','Houston']
# }
# df=pd.DataFrame(data)
# print(df)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       


data={
    "math":90,
    "science":85,
    "english":78
}
series=pd.Series(data)
print(series)
# Accessing elements
print("science marks:",series["science"])
#data type
print("Data type of series:",series.dtype)
# shape
print("Shape of series:",series.shape)