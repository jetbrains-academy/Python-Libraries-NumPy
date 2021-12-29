Each datapoint in our current dataset is in the interval from `0` to `255`.
Since we are going to perform linear algebra operations on this data, 
it might be better to have real numbers between `0` and `1` in each 
entry of the matrices to represent the RGB values. 

### Task
Perform an appropriate operation on the `img` array to achieve a rescaling
such that each datapoint is a real number between `0` and `1`.

You can check whether what you did works by doing some tests. For example, 
inquiring about the maximum and minimum values for this array.


<div class="hint">Division by a scalar is your friend.</div>

<div class="hint">

You can use the [`numpy.ndarray.max()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html) function on the objects of dtype ndarray
without importing NumPy.
</div>