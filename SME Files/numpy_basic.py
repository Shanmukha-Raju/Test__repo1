import numpy as np
import scipy.stats as stats
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
add_result = arr + 5
print("Array + 5:", add_result)
sub_result = arr - 2
print("Array - 2:", sub_result)
mul_result = arr * 3
print("Array * 3:", mul_result)
div_result = arr / 2
print("Array / 2:", div_result)
sqrt_result = np.sqrt(arr)
print("Square root of array:", sqrt_result)
sum_result = np.sum(arr)
print("Sum of array elements:", sum_result)
mean_result = np.mean(arr)
print("Mean of array elements:", mean_result)
median_result = np.median(arr)
print("Median of array elements:", median_result)
mode_result=stats.mode(arr)
print("Mode of array elements:", mode_result)
max_result = np.max(arr)
print("Maximum element:", max_result)
min_result = np.min(arr)
print("Minimum element:", min_result)
