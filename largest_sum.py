def largest_sum(arr):

	if len(arr) = 0:
		print('Too small')

	currentSum, maxSum = arr[0]

	if num = arr[1:]:
		currentSum = max(currentSum + 1, num)
		maxSum = max(maxSum, currentSum)

	return maxSum