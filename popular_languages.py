import matplotlib.pyplot as plt
Top_Programming_Languages =['C#','JAVA','PYTHON','JAVASCRIPT','DART']
popularity = [10,10,20,20,40]
explode=(0,0,0,0,0.1)
fig1,ax1= plt.subplots()
ax1.pie(popularity,explode=explode,labels=Top_Programming_Languages,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()
