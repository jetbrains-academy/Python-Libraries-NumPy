import numpy as np
rng = np.random.default_rng()

temperatures = rng.integers(25, size=7)
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

high = ['High']
low = ['Low']
result = np.where(temperatures > 15, high, low)
warm_days = days[temperatures > 15]

if __name__ == '__main__':
    print(temperatures)
    print(result)
    print(warm_days)


