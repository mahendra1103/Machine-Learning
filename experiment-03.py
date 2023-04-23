#Basic  Numpy Program
#Mahendra Singh Shaktawat 0827CI201103
import numpy as np
 
# Creating array object
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )
 
# Printing type of arr object
print("Array is of type: ", type(arr))
 
# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)
 
# Printing shape of array
print("Shape of array: ", arr.shape)
 
# Printing size (total number of elements) of array
print("Size of array: ", arr.size)
 
# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)









#Some operations using Numpy
#Mahendra Singh Shaktawat 0827CI201103
import numpy as np
 
arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
 
# maximum element of array
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:",
                    arr.max(axis = 1))
 
# minimum element of array
print ("Column-wise minimum elements:",
                        arr.min(axis = 0))
 
# sum of array elements
print ("Sum of all array elements:",
                            arr.sum())
 
# cumulative sum along each row
print ("Cumulative sum along each row:\n",
                        arr.cumsum(axis = 1))









#Sorting using Numpy
#Mahendra Singh Shaktawat 0827CI201103
import numpy as np
 
a = np.array([[1, 4, 2],
                 [3, 4, 6],
              [0, -1, 5]])
 
# sorted array
print ("Array elements in sorted order:\n",
                    np.sort(a, axis = None))
 
# sort array row-wise
print ("Row-wise sorted array:\n",
                np.sort(a, axis = 1))
 
# specify sort algorithm
print ("Column wise sort by applying merge-sort:\n",
            np.sort(a, axis = 0, kind = 'mergesort'))
 
# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
 
# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
            
# Creating array
arr = np.array(values, dtype = dtypes)
print ("\nArray sorted by names:\n",
            np.sort(arr, order = 'name'))
             
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort(arr, order = ['grad_year', 'cgpa']))
                




# Pandas
#Mahendra Singh Shaktawat 0827CI201103
import pandas as pd
import numpy as np
 
# Creating empty series
ser = pd.Series()   
print(ser)
# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
print(ser)



#Mahendra Singh Shaktawat 0827CI201103
import pandas as pd
   
# Calling DataFrame constructor
df = pd.DataFrame()
print(df)
 
# list of strings
lst = ['kuldeep', 'jaydeep', 'mahendra', 'kunal', 
            'nikhilesh', 'himanshu']
   
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)



Matplotlib
#Mahendra Singh Shaktawat 0827CI201103
# importing matplotlib module
from matplotlib import pyplot as plt
 
# x-axis values
x = [5, 2, 9, 4, 7]
 
# Y-axis values
y = [10, 5, 8, 4, 2]
 
# Function to plot
plt.plot(x,y)
 
# function to show the plot
plt.show()

Bar plot : 
#Mahendra Singh Shaktawat 0827CI201103
# importing matplotlib module
from matplotlib import pyplot as plt
 
# x-axis values
x = [5, 2, 9, 4, 7]
 
# Y-axis values
y = [10, 5, 8, 4, 2]
 
# Function to plot the bar
plt.bar(x,y)
 
# function to show the plot
plt.show()

Histogram:
#Mahendra Singh Shaktawat 0827CI201103
# importing matplotlib module
from matplotlib import pyplot as plt
 
# Y-axis values
y = [10, 5, 8, 4, 2]
 
# Function to plot histogram
plt.hist(y)
 
# Function to show the plot
plt.show()
 
Scatter Plot:
#Mahendra Singh Shaktawat 0827CI201103
# importing matplotlib module
from matplotlib import pyplot as plt
 
# x-axis values
x = [5, 2, 9, 4, 7]
 
# Y-axis values
y = [10, 5, 8, 4, 2]
 
# Function to plot scatter
plt.scatter(x, y)
 
# function to show the plot
plt.show()
