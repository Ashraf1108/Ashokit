import pandas as pd

# #example -1 
# data= [10,20,30,40,50]
# df= pd.series(data)
# print(df)

#example -2

# data = {
#     "name":["std1","std2","std3","std4","std5"],
#     "marks":[10,20,30,40,50]
# }
# df= pd.DataFrame(data)
# print(df)
#print(df.head()) # top 5 rows
#print(df.head(4)) # top 4 rows
#print(df.tail(2)) # last 2 rows 
#print(df.sample(2)) # 2 random rows
#print(df.sample(frac=0.5)) # 50% of random data
#print(df.shape) #to know the shape 
#print(df.size) # no of elements
#print(df.ndim) # to know the dimension
#print(df.columns) # to display column name 
#print(df.index) # print the range of indexes 
#print(df.dtypes) # datatypes of columns
#print(df.info()) #to get full info
#print(df.describe()) # this will show first numeric info
#print(df.describe(include="all")) #include all numerical info for all columns
#print(df.iloc[0]) # this is based on pre defined index
#print(df.loc[0]) # this is based on label which we define
#print(df.loc[0:2]) # here 0 is included and 2 is included
#print(df.iloc[0:2]) #here 0 is included and 2 is excluded
#print(df[df['marks']>50])
#print(df[df['marks']==50])
# print(df[df['marks']>50] & (df['marks']<90))
#print(df.sort_values("marks"))
#print(df.sort_values("marks", ascending=False))
#print(df.sort_index())

#df = pd.read_csv("file_name")
#print(df)
#print(df["name"])
#print(df["name","age"])

# print(df.isnull()) # whichever null will show true
# print(df.notnull()) # whichever not null will show true
# print(df.dropna()) #remove the row which contains null 
#print(df.dropna(axis=1)) # remove the column with null
#print(df.fillna(10)) #add 10 to the element which is null
# print(df.ffill()) # it check for null and replaces wiyh previous number from top
# print(df.bfill()) # it checks for null and replaces with previous number from bottom

# print(df["age"].fillna(df["age"].mean())) #for adding missing values with mean 








