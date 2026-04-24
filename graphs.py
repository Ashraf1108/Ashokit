import matplotlib.pyplot as plt
import pandas as pd


# subjects = ["maths","science","english","Computers"]
# marks = [80,90,78,60]
# plt.pie(marks,label=subjects)
# plt.show()



# marks = [85, 90, 75, 80]
# subjects = ['Math', 'Science', 'English', 'History']
# colors = ['red', 'blue', 'green', 'orange']
# explode= [0,0,0.2,0.4]

# plt.pie(marks,
#          labels=subjects,
#            colors=colors, 
#            autopct='%1.1f%%',
#            explode=explode,
#            shadow=True,
#            textprops={'fontsize': 10},
#            wedgeprops={'edgecolor':'red','linewidth':'2'},
#            startangle=90
#            )
# plt.show()
# marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95, 97, 100]

# # result = sum(marks) / 55
# # print(result)

# plt.figure(figsize=(8,6))

# plt.hist(marks,
#          bins=5,
#          color='skyblue',
#          edgecolor='black')
# plt.title("Students marks distribution")
# plt.xlabel("marks")
# plt.ylabel("frequency")
# plt.show()

#scatterplot

# hours = [1,2,3,4,5,6]
# marks=[35,45,50,60,70,85]

# plt.figure(figsize=(8,6))
# plt.scatter(hours,
#             marks,
#             color='red',
#             marker='o',
#             edgecolor='yellow',
#             alpha=0.7)
# plt.grid(True)
# plt.show()


# months=['jan','feb','mar','apr']
# sales = [100,200,300,150]
# plt.fill_between(months,sales)
# plt.xlabel("months")
# plt.ylabel("sales")
# plt.show()


# plt.figure(figsize=(10,8))

# #first graph
# plt.subplot(2,2,1)
# x=[1,2,3,4,5]
# y=[10,20,30,40,50]
# plt.plot(x,y)
# #second graph
# plt.subplot(2,2,2)
# plt.bar(x,y)
# #third graph
# plt.subplot(2,2,3)
# marks = [45, 50, 55, 60, 62, 65, 67, 70
#          , 72, 75, 78, 80, 82, 85, 88, 90
#          , 92, 95, 97, 100]
# plt.hist(marks,
#          bins=5,
#          color='skyblue',
#          edgecolor='black')

# #fourth graph 
# plt.subplot(2,2,4)
# subjects = ["maths","science","english","Computers"]
# marks = [80,90,78,60]
# #plt.pie(marks,label=subjects)
# plt.pie(marks, labels=subjects)
# plt.show()
