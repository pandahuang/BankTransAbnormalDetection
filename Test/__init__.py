__author__ = 'panda_huang'
import numpy as np
from numpy.matlib import randn


if __name__ == '__main__':
    data1 = [6, 7.5, 8, 0 ,1]
    # Create an array.
    arr1 = np.array(data1)
    print(arr1)

    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    print(arr2)
    # Type of data in array.
    print(arr1.dtype)
    print(arr2.ndim)
    print(arr2.shape)

    print(np.zeros(10))
    print(np.zeros((3, 6)))
    # Empty array will contain uninitialized garbage values.
    print(np.empty((2, 3, 2)))

    # arange is an array-valued version of the built-in Python range function:
    print(np.arange(15))

    arr3 = np.array([1, 2, 3], dtype=np.float64)
    arr4 = np.array([1, 2, 3], dtype=np.int32)
    print(arr3.dtype)
    print(arr4.dtype)

    arr5 = np.array([1, 2, 3, 4, 5])
    print(arr5.dtype)
    arr6 = arr5.astype(np.float64)
    print(arr6.dtype)

    # Operations between Arrays and Scalars
    arr = np.array([[1., 2., 3.], [4., 5., 6.]])
    print(arr * arr)
    print(arr - arr)

    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(arr2d[2])
    arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    old_values = arr3d[0].copy()
    print('------------')
    arr3d[0] = 42
    print(arr3d)
    arr3d[0] = old_values
    print(arr3d)

    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    print(names)
    data = randn(7, 4)
    print(data)

    # Boolean Indexing
    # Suppose each name corresponds to a row in the data array. If we wanted to select all
    # the rows with corresponding name 'Bob'. Like arithmetic operations, comparisons
    # (such as ==) with arrays are also vectorized. Thus, comparing names with the string
    # 'Bob' yields a boolean array:
    print(names == 'Bob')
    print(data[names == 'Bob'])
    print(data[names == 'Bob', 2:],)
    print(data[names == 'Bob', 3])
    print(data[((names == 'Bob') | (names == 'Will'))])

    # Fancy Indexing
    # Fancy indexing is a term adopted by NumPy to describe indexing using integer arrays.
    arr = np.empty((8, 4))
    for i in range(8):
        arr[i] = i
    print(arr)
    print('To select out a subset of the rows in a particular order, you can simply pass a list or ndarray of integers specifying the desired order:')
    print(arr[[4, 3, 0, 6]])
    print('Hopefully this code did what you expected! Using negative indices select rows from the end:')
    print(arr[[-3, -5, -7]])
    print('Passing multiple index arrays does something slightly different; it selects a 1D array of elements corresponding to each tuple of indices:')
    arr = np.arange(32).reshape((8, 4))
    print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

    print('Transposing is a special form of reshaping which similarly returns a view on the underlying data without copying anything.')
    arr = np.arange(15).reshape((3, 5))
    print(arr.T)

    print('''A universal function, or ufunc, is a function that performs elementwise operations on
data in ndarrays. You can think of them as fast vectorized wrappers for simple functions
that take one or more scalar values and produce one or more scalar results.''')
    arr = np.arange(10)
    print(np.sqrt(arr))
    print(np.exp(arr))
    x = randn(8)
    y = randn(8)
    print(x)
    print(y)
    print(np.maximum(x, y))
    print('''While not common, a ufunc can return multiple arrays. modf is one example, a vectorized
version of the built-in Python divmod: it returns the fractional and integral parts of
a floating point array:''')
    arr = randn(7) * 5
    print(np.modf(arr))

    # Expressing Conditional Logic as Array Operations
    print('''The numpy.where function is a vectorized version of the ternary expression x if condi
tion else y.''')
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    print('''Suppose we wanted to take a value from xarr whenever the corresponding value in
cond is True otherwise take the value from yarr.''')
    result = np.where(cond, xarr, yarr)
    print(result)
    arr = randn(4, 4)
    print(np.where(arr > 0, 2, -2))

    # Mathematical and Statistical Methods
    arr = np.random.randn(5, 4) # normally-distributed data
    print(arr)
    print(arr.mean())
    print(np.mean(arr))
    print(arr.sum())
    print(arr.mean(axis=1))

    # Methods for Boolean Arrays
    print('Boolean values are coerced to 1 (True) and 0 (False) in the above methods. Thus, sum is often used as a means of counting True values in a boolean array:')
    arr = randn(100)
    print((arr > 0).sum())
    bools = np.array([False, False, True, False])
    print(bools.any())
    print(bools.all())

    arr = randn(8)
    print(arr)
    print(np.sort(arr))

    # Unique and Other Set Logic
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    print(np.unique(names))
    ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
    print(np.unique(ints))