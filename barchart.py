import matplotlib.pyplot as plt
categories=['apple','banana','cherris','dates','elderberries']
values=[10,24,36,18,12]
plt.bar(categories,values,color='coral',edgecolor='black')
plt.xlabel('Fruit Sales')
plt.ylabel('Fruit Type')
plt.title('Units sold')
plt.show()