## This demo

This is a demo of NumPy tutorial available at JetBrains Academy. Here we will showcase a few selected steps of developing a simple image compression algorithm. 
The demo has most of the code provided from the start leaving you to fill in the gaps. Details of the implementation are discussed in hints, if you are interested and have spare time.

Good luck and have fun!


## Task


Let's load the image of a horse provided in the project. Type the file name `horse.jpg` into the highlighted placeholder.

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

**Do not forget to run the code! (&shortcut:Run;)**



