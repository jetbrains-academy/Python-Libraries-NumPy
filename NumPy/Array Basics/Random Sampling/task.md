## Random Sampling

Sometimes you might need to fill an array with random numbers or sample them from 
different statistical distributions. 
Numpy's `random` module allows you to do this. It is a suite of functions based on 
pseudorandom number generation. It is called pseudorandom because "random" means something that 
can not be predicted logically, and if a program generates a "random" number 
it can be predicted, thus it is not truly random.

The function `numpy.random.random` returns random floats in the half-open interval `[0.0, 1.0)`:

```python
a = np.random.random(5)
print(a)
```
Output:
```text
[0.73719247 0.38265166 0.48330973 0.27551432 0.88136674]
```

### Random Generator
Call [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng) 
to get a new instance of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator), 
then call its methods to obtain samples from different distributions. 
```python
rng = np.random.default_rng()
a = rng.integers(1000)  # Randomly pick one integer from 0 to 1000
print(a)
```
Output:
```text
346
```
`random.Generator.integers` returns random integers from a half-open interval: low (inclusive) to high (exclusive), 
or if you specify `endpoint=True`, then the interval is closed: low (inclusive) to high (inclusive).
Integers are returned from the "discrete uniform" distribution.

Print 10 random integers from the interval `[0, 2)`:

```python
print(rng.integers(2, size=10)) 
```
Output:
```text
[1 1 0 1 0 0 0 1 0 0]
```
Generate a 2 x 4 array of integers between `0` and `4`, inclusive:
```python
print(rng.integers(4, size=(2, 4), endpoint=True))
```
Equivalent to:
```python
print(rng.integers(5, size=(2, 4)))
```
Output:
```text
[[1 2 0 3]
 [4 2 4 3]]
```

### Task
Using the function [`numpy.random.Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html?highlight=random%20normal#numpy.random.Generator.normal), 
draw 1000 samples from the normal distribution with mean equal to `1` and standard deviation equal to `0.5`.
You can visualize your sample and make sure the mean and variance are ok by running the script – we predefined the 
code for that in the `if __name__ == '__main__':` block.