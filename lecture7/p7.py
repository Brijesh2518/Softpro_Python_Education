# how to flatten an array
'''
from numpy import*
arr1 = array([
            [1,2,3],
            [4,5,6]
            ])
arr2 = arr1.flatten()
print(arr2)
'''
# how to reshpae an array

from numpy import*
arr1 = array([
            [1,2,3],
            [4,5,6]
            ])
arr2 = arr1.flatten()
arr3 = arr2.reshape(3,2)
print(arr3)