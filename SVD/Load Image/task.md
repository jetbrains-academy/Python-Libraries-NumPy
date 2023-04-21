## This demo

This is a demo of NumPy tutorial available at JetBrains Academy. Here we will showcase a few selected steps of developing a simple image compression algorithm. For the information about the tutorial itself see the *Details* below.

The demo has most of the code provided from the start leaving you to fill in the gaps. Details of the implementation are discussed in hints, if you are interested and have spare time.

Good luck and have fun!

<details>

#### Who is the initial tutorial for?
This tutorial is for people who have a basic understanding of linear algebra and arrays in NumPy and
want to find out how n-dimensional (n >= 2) arrays are represented and manipulated. In particular,
if you are curious how to apply common functions to n-dimensional arrays (without using for-loops)
or if you want to understand axis and shape properties for n-dimensional arrays, this tutorial might be of help.


#### Learning Objectives
After completing this tutorial, you should be able to:

- understand the difference between one-, two-, and n-dimensional arrays in NumPy;

- apply some linear algebra operations to n-dimensional arrays without using for-loops;

- understand axis and shape properties for n-dimensional arrays.

#### Content

The lesson is based on the NumPy tutorial ["Linear algebra on n-dimensional arrays"](https://numpy.org/numpy-tutorials/content/tutorial-svd.html).




<i>Apart fom NumPy, in this lesson, we will be using another library called `matplotlib`. 
We won't discuss it in detail here, but there's going to be a separate chapter of the course 
dedicated to this library. For now, if you wish to find out more about it, please 
refer to the [docs](https://matplotlib.org/stable/users/index.html).
Matplotlib is a widely used comprehensive library for creating static, animated, and interactive visualizations in Python.</i>
</details>

Image compression is a very useful thing because it allows saving images without taking up large amounts of memory (data approximation).
In this lesson, we will use a [matrix decomposition](https://en.wikipedia.org/wiki/Matrix_decomposition) from linear algebra,
the singular value decomposition, to generate a compressed approximation of an image while still retaining many of the original features.

In order to transform your image into a NumPy array that can be manipulated, you can use the 
`imread` function from the `matplotlib.pyplot` submodule (line 2 in the code editor). 


Now, `img` is a NumPy array, as we can see when using the `type` function.


<div class="hint" title="Image conversion">

For more information on how images are treated when converted to NumPy arrays, 
see [A crash course on NumPy for images](https://scikit-image.org/docs/stable/user_guide/numpy_images.html) from the `scikit-image` documentation.
</div>

### Task

Let's load the image of a horse provided in the project.

Then we will check the number of dimensions in our array and print its shape. 

<div class="hint" title="Shape of an array">
Since this image is two-dimensional
(the pixels in the image form a rectangle), we might expect a two-dimensional array to
represent it (a matrix). However, using the `ndim` and `shape` properties of this NumPy array gives us a
different result.

The output of `shape` is a tuple with three elements, which means that this is a three-dimensional array.
In fact, since this is a color image and we used the `imread` function to read it, the
data is organized in three 2D arrays representing color channels (in this case, red, green,
and blue – RGB). You can see this by looking at the shape: it indicates that we have an
array of 3 matrices, 408x612 each.
</div>

**Do not forget to run the code!**



