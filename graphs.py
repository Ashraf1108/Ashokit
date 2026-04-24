import matplotlib.pyplot as plt
import pandas as pd


# subjects = ["maths","science","english","Computers"]
# marks = [80,90,78,60]
# plt.pie(marks,label=subjects)
# plt.show()

subjects = ["maths","science","english","Computers"]
marks = [80,90,78,60]
colors = ['gold','silver','brown','yellow']
plt.pie(marks,label=subjects,color=colors,autopct='%1.1f%%')
plt.show()