If you have worked before with only one- or two-dimensional arrays in NumPy, 
you might have used `numpy.dot` and `numpy.matmul` (or the `@` operator) interchangeably. 
However, for n-dimensional arrays, they work in very different ways. 
For more details, check the documentation on [`numpy.matmul`](https://numpy.org/devdocs/reference/generated/numpy.matmul.html#numpy.matmul).

### Task
Now, to build our approximation, we first need to make sure that our singular 
values are ready for multiplication, so we build our `Sigma` matrix similarly 
to what we did before. The `Sigma` array must have dimensions `(3, 408, 612)`. 
In order to add the singular values to the diagonal of `Sigma`, we will again 
apply the `fill_diagonal` function, using each of the 3 rows in `s` as the diagonal 
for each of the 3 matrices in `Sigma`.

To rebuild the full SVD with no approximation, we can compute a product of 
`Sigma` and the orthogonal matrices `U` and `Vt`.

After running the script, note the shape of `reconstructed`.

The reconstructed image should be indistinguishable from the original one, except 
for differences due to floating point errors from the reconstruction. Remember that 
our original image consisted of floating point values in the range `[0., 1.]`. 
The accumulation of floating point error from the reconstruction can result in 
values slightly outside this original range (check out the output of the second print statement in `main`).
Since `imshow` expects values in the range, we can use [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.clip.html) to excise the floating point error:

```python
reconstructed = np.clip(reconstructed, 0, 1)
```

In fact, `imshow` peforms this clipping under-the-hood, so if you skip 
this line, you might see a warning message saying `"Clipping input data 
to the valid range for imshow with RGB data ([0..1] for floats or [0..255] for integers)."`