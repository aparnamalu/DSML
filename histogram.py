import matplotlib.pyplot as plt
values=[10,24,36,18,12]
plt.hist(values,bins=5,color='skyblue',edgecolor='black')
plt.xlabel('Fruit Sales')
plt.ylabel('Fruit Type')
plt.title('Units sold')
plt.show()