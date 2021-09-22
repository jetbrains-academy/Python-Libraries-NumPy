## Reshape

Reshaping means changing the `shape` of an array without changing its data.
As we mentioned earlier, the `shape` of an array is the number of elements in each dimension.
By reshaping we can add or remove dimensions or change the number of elements in each dimension.

The function [`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape) 
is used for reshaping, and it accepts three arguments:

- The array to be reshaped.
- The new shape as an `int` or tuple of `int`s.
- An optional argument `order`, which defines the order in which the elements are read and placed into the reshaped array.

### Examples
1. Reshape 1D array into a 2D array:
```python
a = np.arange(10)
print(np.reshape(a, (2, 5)))
```
Output:
```text
[[0 1 2 3 4]
 [5 6 7 8 9]]
```
2. Reshape a 2D array into a 1D array:
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.reshape(a, 6))
```
Output:
```text
[1 2 3 4 5 6]
```

The latter can also be achieved by using `numpy.ndarray.flatten`:
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.flatten())
```
Output:
```text
[1 2 3 4 5 6]
```

### Task
1. Create an array `a` of integers in the interval from `12` to `30` with step `3`.
2. Reshape it so that it has 2 rows and 3 columns.

<div class="hint">For (1) you can use the <code>arange</code> function.</div>