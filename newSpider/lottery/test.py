import matplotlib.pyplot as plt
labels=['frogs','hogs','dogs','logs']
sizes=[15,20,45,180]
colors='yellowgreen','gold','lightskyblue','lightcoral'
# explode=0,0.5,0,0
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=50)
plt.axis('equal')
plt.show()