## Indexing Basics

Array indexing refers to any use of the square brackets (`[]`) to index array values.

### Single element indexing

Single element indexing for a 1-D array works exactly like that 
for other standard Python sequences. It is 0-based, and accepts negative indices for 
indexing from the end of the array.

Unlike lists and tuples, NumPy arrays support multidimensional indexing for multidimensional 
arrays. That means that **it is not necessary to separate each dimension’s index into its 
own set of square brackets**.

```python
x = np.arange(10).reshape(2, 5) # 2-dimensional
print(x[1, 3])
print(x[1, -1])
print(x[0])
```
Output:
```text
8
9
[0, 1, 2, 3, 4]
```
Note that `x[0, 2]` and `x[0][2]` will produce the same result, `2`. However, the second case 
is less efficient as a new temporary array is created after the first index that is subsequently 
indexed by 2.

### Slicing

It is possible to slice arrays to extract arrays of the same number of dimensions, 
but of different sizes than the original. The slicing works exactly the same way it 
does for lists and tuples except that they can be applied to multiple dimensions as well.
Basic slicing occurs when obj is a slice object (constructed by `start:stop:step` notation inside 
of brackets), an integer, or a tuple of slice objects and integers.

1-D array:
```python
x = np.arange(35)
print(x[2:15])
print(x[1:30:5])  # [start:stop:step]
```
Output:
```text
[ 2  3  4  5  6  7  8  9 10 11 12 13 14]
[ 1  6 11 16 21 26]
```
2-D array:
```python
y = x.reshape(5, 7)
print(y[1:5:2])
print(y[1:5:2, ::3])  # First slicing in the first dimension, then in the second.
```
Output:
```text
[[ 7  8  9 10 11 12 13]
 [21 22 23 24 25 26 27]]
[[ 7 10 13]
 [21 24 27]]
```

These examples show the use of indexing when referencing data in an array. 
They work just as well when assigning to an array.
Read more about this topic [here](https://numpy.org/doc/stable/user/basics.indexing.html#basics-indexing).

### Task
1. Variable `a`: use indexing on the array `x` to extract number `19` from it. Please
   **do not** just assign `a` the value `19` :)
2. Variable `b`: use slicing to extract every second element in every second row. The resulting array 
should have shape `(5, 2)`.
   