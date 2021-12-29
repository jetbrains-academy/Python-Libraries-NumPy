<i>Apart fom NumPy, in this lesson, we will be using another library called `matplotlib`. 
We won't discuss it in detail here, but there's going to be a separate chapter of the course 
dedicated to this library. For now, if you wish to find out more about it, please 
refer to the [docs](https://matplotlib.org/stable/users/index.html).
Matplotlib is a widely used comprehensive library for creating static, animated, and interactive visualizations in Python.</i>

In order to transform your image into a NumPy array that can be manipulated, you can use the 
`imread` function from the `matplotlib.pyplot` submodule (line 2 in the code editor). 


Now, `img` is a NumPy array, as we can see when using the `type` function.


<div class="hint">

For more information on how images are treated when converted to NumPy arrays, 
see [A crash course on NumPy for images](https://scikit-image.org/docs/stable/user_guide/numpy_images.html) from the `scikit-image` documentation.
</div>

### Task

- First, let's check the number of dimensions in our array.

- Then, print the shape of the array. 


Since this image is two-dimensional 
(the pixels in the image form a rectangle), we might expect a two-dimensional array to 
represent it (a matrix). However, using the `ndim` and `shape` properties of this NumPy array gives us a 
different result.

The output of `shape` is a tuple with three elements, which means that this is a three-dimensional array. 
In fact, since this is a color image and we used the `imread` function to read it, the 
data is organized in three 2D arrays representing color channels (in this case, red, green, 
and blue – RGB). You can see this by looking at the shape: it indicates that we have an 
array of 3 matrices, 408x612 each.


