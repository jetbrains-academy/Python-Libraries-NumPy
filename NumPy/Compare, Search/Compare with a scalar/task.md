## Compare with a scalar

Each element of an array can be compared against a scalar using any of the operators:
- greater (`>`),
- greater equal (`>=`), 
- smaller (`<`), 
- smaller equal (`<=`),
- equal (`==`).

This is accomplished due to the [broadcasting](course://NumPy/Array Basics/Broadcasting) feature. 
For example, the comparison `arr > x` results in an array of boolean values resulting from the element-wise comparisons:
```python
arr = np.arange(10)
print(arr > 3)
```
Output:
```text
[False False False False  True  True  True  True  True  True]
```
You already saw such arrays in the task [Boolean Indexing](course://NumPy/Array Indexing and Slicing/Boolean Indexing).

### Task
Your task is to create the array `filtered_arr` such that it only contains the numbers from the original
array `arr` that are divisible by `4`.

<div class="hint">Use boolean indexing.</div>