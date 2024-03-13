#CREATION OF 2D ARRAY

from numpy import*
arr1 = array([
            [1,2,3],
            [4,5,6]
            ])
print(arr1.ndim)  # how to check the dimentions of the array
print(arr1.shape)  #how to check the shape (rows,column) of the array
print(arr1.size)   # How to check total elements 
arr2 = arr1.flatten() # how to flatten an array