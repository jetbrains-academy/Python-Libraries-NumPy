The way images are represented (as a 3D matrix) can
ultimately result in a large amount of memory used to
produce a single image. 

For instance, to save a
100 × 100 image in grayscale, 10,000
different pixel values would be stored.


One way to enable computers to save images without taking up large amounts of memory (to approximate the data) is
to use methods from linear algebra, such as [Singular Value
Decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition) (SVD).

<div class="hint" title="Grayscale">

 It allows compressing the size of the saturation
matrices while retaining the most important components, i.e., saving
an image using less memory while preserving the image
quality.

Here, we will use the SVD to rebuild an image that
uses less singular value information than the original one while still retaining many of its features.



In order to extract information from a given matrix, we can use the SVD to obtain 3 arrays which
can be multiplied to obtain the original matrix. 


Note that according to [colorimetry](https://en.wikipedia.org/wiki/Grayscale#Colorimetric_(perceptual_luminance-reserving)_conversion_to_grayscale), it is possible to obtain a fairly
reasonable grayscale version of our color image if we apply the formula:

Y = 0.2126R + 0.7152G + 0.0722B

where Y is the array representing the resulting grayscale image, and R, G, and B are the red,
green, and blue channel arrays we had originally. 
</div>


Let’s first see how the SVD works in practice with just one matrix.



## Task 

Use matrix multiplication (**@**) in the highlighted placeholder.
Run the script to see the result.

<div class="hint" title="Colormap">
We should use a colormap from `matplotlib` 
corresponding to the color we wish to see in our image.
In our case, we are approximating the grayscale portion of the image, so we will use the colormap `gray`.
Otherwise, matplotlib will default to a colormap that does not correspond to the real data. 
You can try dropping the `cmap` argument and see what happens.

</div>

<div class="hint" title="How to multiply - @">

Notice that here we can use the `@` operator 
(the matrix multiplication operator for NumPy arrays, see [`numpy.matmul`](https://numpy.org/devdocs/reference/generated/numpy.matmul.html#numpy.matmul)).
</div>


**Do not forget to run the code! (&shortcut:Run;)**