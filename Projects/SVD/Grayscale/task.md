Let’s first see how the SVD works in practice with just one matrix.
Note that according to [colorimetry](https://en.wikipedia.org/wiki/Grayscale#Colorimetric_(perceptual_luminance-reserving)_conversion_to_grayscale), it is possible to obtain a fairly
reasonable grayscale version of our color image if we apply the formula:

$$Y = 0.2126R + 0.7152G + 0.0722B$$

where $Y$ is the array representing the resulting grayscale image, and $R$, $G$, and $B$ are the red,
green, and blue channel arrays we had originally. 

### Task 

Use matrix multiplication and the equation above to obtain a grayscale version of the image.
Run the script to see the result.

We should use a colormap from `matplotlib` 
corresponding to the color we wish to see in our image.
In our case, we are approximating the grayscale portion of the image, so we will use the colormap `gray`.
Otherwise, matplotlib will default to a colormap that does not correspond to the real data. 
You can try dropping the `cmap` argument and see what happens.

<div class="hint">

Notice that here we can use the `@` operator 
(the matrix multiplication operator for NumPy arrays, see [`numpy.matmul`](https://numpy.org/devdocs/reference/generated/numpy.matmul.html#numpy.matmul)).
</div>