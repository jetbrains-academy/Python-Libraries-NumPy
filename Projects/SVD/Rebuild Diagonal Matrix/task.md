Note that `s` has a particular shape: it has only one dimension. 
This means that some linear algebra functions that expect 2D arrays might not work here. 
For example, from the theory, one might expect `s` and `Vt` to be compatible for multiplication. 
However, this is not true, as `s` does not have a second axis. Executing `s @ Vt`
results in a `ValueError`. This happens because having a one-dimensional array for `s` 
in this case, is much more economical in practice than building a diagonal matrix with the 
same data. 

### Task

To reconstruct the original matrix, we can rebuild the diagonal matrix $\Sigma$
with the elements of `s` in its diagonal and with the appropriate dimensions for multiplying: 
in our case, $\Sigma$ should be 408x612, since `U` is 408x408 and `Vt` is 612x612. 

In order to add the singular values to the diagonal of `Sigma`, 
we will use the [`fill_diagonal`](https://numpy.org/devdocs/reference/generated/numpy.fill_diagonal.html) function from NumPy.

Now, we want to check if the reconstructed `U @ Sigma @ Vt` is close to 
the original `img_gray` matrix.

The `linalg` module includes a [`norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html) function, which computes the norm of a vector or 
matrix represented in a NumPy array. For example, from the SVD explanation above, 
we would expect the norm of the difference between `img_gray` and the reconstructed 
SVD product to be small. After running the script, you should see something like
`1.2008248445342685e-12` on the second line of your output.
(The actual result of this operation might be different depending on your 
architecture and linear algebra setup. Regardless, you should see a small number.)

We could also use the [`numpy.allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html) function to make sure the reconstructed product 
is, in fact, close to our original matrix (the difference between the two arrays is small).
The third `print` statement should print `True`.



