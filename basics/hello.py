import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
nums = list(map(int, input_data[1:n+1]))

print("Input numbers:", nums)
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sorted:", sorted(nums))
print("Reversed:", sorted(nums, reverse=True))