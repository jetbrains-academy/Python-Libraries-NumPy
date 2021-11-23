Note that `s` has a particular shape: it has only one dimension. 
This means that some linear algebra functions that expect 2d arrays might not work. 
For example, from the theory, one might expect s and Vt to be compatible for multiplication. 
However, this is not true as `s` does not have a second axis. Executing `s @ Vt`
results in a `ValueError`. This happens because having a one-dimensional array for `s`, 
in this case, is much more economic in practice than building a diagonal matrix with the 
same data. 

### Task

To reconstruct the original matrix, we can rebuild the diagonal matrix $\Sigma$
with the elements of `s` in its diagonal and with the appropriate dimensions for multiplying: 
in our case, $\Sigma$ should be 408x612 since `U` is 408x408 and `Vt` is 612x612. 

In order to add the singular values to the diagonal of `Sigma`, 
we will use the [`fill_diagonal`](https://numpy.org/devdocs/reference/generated/numpy.fill_diagonal.html) function from NumPy.

Next, we want to check if the reconstructed `U @ Sigma @ Vt` is close to 
the original `img_gray` matrix.

