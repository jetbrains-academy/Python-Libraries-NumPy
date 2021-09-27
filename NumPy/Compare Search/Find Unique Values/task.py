import numpy as np

csv = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
data, labels = csv[:, 1:], np.array(csv[:, 0], dtype=np.int64)

classes = np.unique(labels)
unique_measurements, unique_data_counts = np.unique(data, return_counts=True)

most_frequent_index = np.argmax(unique_data_counts)
most_frequent_measurement = unique_measurements.flatten()[most_frequent_index]

if __name__ == "__main__":
    print(classes)
    print(unique_data_counts)
    print(most_frequent_index)
    print(most_frequent_measurement)

