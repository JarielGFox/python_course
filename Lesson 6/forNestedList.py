multiDimensionalArray = ['Gianluca', 26, 90, ['Insalata', 'Patate', 'Pollo']]

'''questo non si può fare perchè va in type error
for i in range(len(multiDimensionalArray)):
    for j in range(len(multiDimensionalArray[i])):
        print(multiDimensionalArray[i][j])
'''
    
multiDimensionalArray[2] = 100
print(multiDimensionalArray)
