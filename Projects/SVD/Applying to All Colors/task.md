Now, we want to do the same kind of operation, but with all three colors. 
Our first instinct might be to repeat the same operation we did before 
on each color matrix individually. However, NumPy’s broadcasting takes 
care of this for us.

If our array has more than two dimensions, then the SVD can be applied 
to all axes at once. However, the linear algebra functions in NumPy 
expect to see an array of the form `(n, M, N)`, where the first axis `n` 
represents the number of `MxN` matrices in the stack.

In our case, `img_rescaled.shape` is `(408, 612, 3)`,
so we need to permute the axes of this array to get a shape like `(3, 408, 612)`. 
Fortunately, the `numpy.transpose` function can do that for us:

```python
np.transpose(x, axes=(i, j, k))
```
It indicates that the axes will be reordered such that the final shape of 
the transposed array will be reordered according to the indices `(i, j, k)`.

After transposing the matrix, we will be ready to apply the SVD.

### Task
1. Transpose the `img_rescaled` matrix so that the SVD could be applied to it.
2. Apply the SVD.

Note the shapes of `U`, `s`, and `Vt`. In order to build the final approximation 
matrix, we must understand how multiplication across different axes works.
