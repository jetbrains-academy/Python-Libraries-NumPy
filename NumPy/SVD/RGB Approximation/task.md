Now, to perform the approximation, we must choose only the first `k` singular values 
for each color channel.

### Task

You should select only the first `k` components of the last axis for `Sigma` 
(this means that we use only the first `k` columns of each of the three 
matrices in the stack), and only the first `k` components 
in the second-to-last axis of `Vt` (this means we select only the first 
`k` rows from every matrix in the stack `Vt` and all columns). 

The shape of the resulting array will be `(3, 408, 612)`, which
is not the right shape for showing the image. In `main`, reorder the axes back 
to our original shape to that you can see the approximation when running the script.
This part of the task is not checked, but you probably want to complete it to see the result!

Try running this with different values of `k`.

Even though the image is not as sharp, using only a small number of `k` singular values 
(compared to the original set of 408 values), we can recover many of the distinguishing 
features from this image.

<div class="hint">To get the approximation, calculate the product of three matrices once again,
but slice them to keep only the components you need.</div>

<div class="hint">The initial reordering of the axes was done on line 9. You can use the same operation.</div>

<div class="hint"> 

The suggested solution uses [ellipsis](https://numpy.org/devdocs/user/basics.indexing.html#dimensional-indexing-tools) syntax. Ellipsis expands to the number of `:` objects needed 
for the selection tuple to index all dimensions.
</div>

