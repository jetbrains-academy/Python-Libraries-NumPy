Now, applying the [`linalg.svd`](https://numpy.org/devdocs/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd) 
function to the `img_gray` matrix, we can obtain its decomposition.

### Task

Use the SVD decomposition to obtain orthogonal matrices `U` and `Vt` and the diagonal 
matrix `s` from the `img_gray` matrix.
Run the script to see if the result is what we would expect for a 408 x 612 image.

<div class="hint">
Expected result: (408, 408) (408,) (612, 612).
</div>

<div class="hint">
Note that with a larger image, this might take a while to run, depending on the 
size of the image and your hardware. This is normal! The SVD can be a pretty intensive computation.
</div>


