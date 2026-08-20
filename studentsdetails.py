import pandas as pd
data={
    'Roll.No':[1,2,3,4,5],
    'Name':['Nithin','Asha','Naveen','John','Neha'],
    'Age':[20,21,22,20,23],
    'Marks':[85,76,92,67,88]
}
students=pd.DataFrame(data)
print("Student Table:")
print("Students")
print("\n(b)students with marks greater than 80:")
print(students[students['Marks']>80])
names_starting_with_N=students[students['Name'].str.startswith('N')]
remaining_names=students[~students['Name'].str.startswith('N')]
print("\n(c1)students whose names starting with 'N':")
print(names_starting_with_N)
print("\n(c2)remaining students:")
print(remaining_names)

