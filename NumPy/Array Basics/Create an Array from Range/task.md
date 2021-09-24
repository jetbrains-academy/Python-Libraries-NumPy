## Create an Array from Range

To create arrays containing sequences of numbers, NumPy provides the [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html?highlight=arange#numpy.arange) 
function. It is analogous to the Python built-in [`range`](https://docs.python.org/3/library/functions.html#func-range), but returns an array.

```python
a = np.arange(10, 100, 10) # 10 is start, 100 is stop, 10 is step
b = np.arange(0, 5, 0.5)
print(a)
print(b)
```
Output:
```text
[10 20 30 40 50 60 70 80 90]
[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
```

Due to the finite floating point precision, it is generally not possible to predict
the number of elements obtained when `arange` is used with floating point arguments.
Therefore, in most cases it is better to use the function [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace), which receives
the number of elements that we want as an argument instead of the step:

```python
a = np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
print(a)
```
Output:
```text
[0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
```
`linspace` returns a specified number of evenly spaced samples over the specified interval.

### Task
Complete the implementation on the function `sine_array()`:
1) Use `numpy.linspace` function to create an array `x` of `num` numbers from `start` to `stop`
2) Create an array `f` of numbers, such that $f = sin(x)$
3) In `if __name__ == '__main__':` call the function to create an array `a` of $100$ numbers from $0$ to $3 * pi$
and the corresponding array `b`. 
   
We added some code to plot the resulting data: run the script to see the plot.

<div class="hint">
Use the <a href="https://numpy.org/doc/stable/reference/generated/numpy.sin.html?highlight=sin#numpy.sin"><code>numpy.sin</code></a> function for the <code>f</code> array.
</div>