# two sum

arr = [2,4,-3,7,8,5]
target = 15

# brute force 2 loops 
# time complexity - O(n^2) 
# space complexity - O(1)

def BruteForce(arr, target):

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] + arr[j] == target:
				return [i, j]

print(BruteForce(arr, target))



# using hashTable 
# time complexity - O(n)
# space complexity - O(n)

def usingDic(arr, target):
	hashDic = {}

	for num in arr:
		toFind = target - num

		if toFind in hashDic:
			return toFind, num
		else:
			hashDic[num] = True


print(usingDic(arr, target))



# sort to min-max
# time complexity - O(nlog(n))
# space complexity - O(1)

def sortAndDone(arr, target):
	arr.sort()
	minVal = 0
	maxVal = len(arr) - 1

	while minVal < maxVal:
		if arr[minVal] + arr[maxVal] == target:
			return minVal, maxVal
		elif arr[minVal] + arr[maxVal] > target:
			maxVal -= 1
		elif arr[minVal] + arr[maxVal] < target:
			minVal += 1
	return []

print(sortAndDone(arr, target))



