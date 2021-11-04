## Random Shuffle

Sometimes you need to shuffle the contents of an array. For instance, in machine learning tasks 
it is common to shuffle data and normalize it. 

NumPy offers two methods that will provide you with randomly shuffled (or **permuted**) data:
- [`random.Generator.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation): randomly permutes a sequence, or return a permuted range.
- [`random.Generator.shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle): modifies an array or sequence **in-place** by shuffling its contents.

The key difference between these two methods is that `permutation` returns an array, while
`shuffle` modifies it in-place. Additionally, `permutation` allows you to create a permuted sequence from 
range. For arrays with more than one dimension, the order of sub-arrays is changed but their contents remains the same.
Please check out the examples below.

1. Shuffle / permute a sequence
```python
rng = np.random.default_rng()
print(rng.permutation(10))  # permutation returns a permuted range
```
Output (will be different every time):
```text
[6 5 0 4 9 1 8 2 3 7]
```

```python
arr = np.arange(10)
rng.shuffle(arr)  # Shuffle sequence in place
print(arr)
```
Output:
```text
[0 3 5 7 8 6 9 1 2 4]
```
2. Shuffle / permute a 2D array
```python
arr = np.arange(9).reshape((3, 3))
print(rng.permutation(arr))  # permutation returns a permuted array, order within rows is maintained
```
Output:
```text
[[3 4 5]
 [6 7 8]
 [0 1 2]]
```
```python
arr = np.arange(9).reshape((3, 3))
rng.shuffle(arr) # Shuffle array in place, order within rows is maintained
print(arr)
```
Output:
```text
[[6 7 8]
 [3 4 5]
 [0 1 2]]
```
2. Shuffle / permute a 2D array along another axis
```python
arr = np.arange(9).reshape((3, 3))
print(rng.permutation(arr, axis=1))  # permutation returns an array permuted within rows
```
Output:
```text
[[2 0 1]
 [5 3 4]
 [8 6 7]]
```
```python
arr = np.arange(9).reshape((3, 3))
rng.shuffle(arr, axis=1) # Shuffle array in place within rows
print(arr)
```
Output:
```text
[[0 2 1]
 [3 5 4]
 [6 8 7]]
```

### Task

First, `shuffle` the rows of the array `arr` (0th axis is the default axis).
Then, randomly permute the numbers within rows in `arr` and assign the result to
the variable `permuted_2d`.
Still, your array is not fully random, since all the elements remain in the same rows
where they started. Create a `fully_random` array. Use some of the methods we
learned earlier.

<div class="hint">Use the examples in task description to shuffle and permute the array.</div>

<div class="hint">To fully randomize it, you could first, <code>flatten</code> the array, apply the <code>permutation</code>
method to it, and <code>reshape</code> back to the original shape. All these things can be done in one
line of code (although this does not mean that they always should).</div>
