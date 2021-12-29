NumPy refers to each dimension as an <i>axis</i>.
Because of how `imread` works, the first index in the 3rd axis is the red pixel data for our image. 
The second contains green and the third one – blue.
We can access this by using the slicing syntax.

### Task
Get an array of red pixel data by slicing the original `img` array. 

<div class="hint">You need to slice it in a way that keeps everything in the first and second 
dimensions and only the first elements in the third.</div>

Afterwards, check out the shape of the array by running the script. 
From the output, we can see that every value in `red_pixel_data` is an integer value between 
0 and 255, representing the level of red in each corresponding image pixel.
As expected, this is a 408x612 matrix.