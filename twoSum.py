# two sum

arr = [2,4,-3,7,8,5]
target = 15

# brute force - 2 loops - time complexity - O(n^2) space complexity - O(1)

def BruteForce(arr, target):

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if arr[i] + arr[j] == target:
				return [i, j]

#print(BruteForce(arr, target))

def usingDic(arr, target):
	hashDic = { }
	for i in range(len(arr)):
		hashDic[arr[i]] = i

	for i, val in enumerate(hashDic):

		toFind = target - val

		if toFind in hashDic:
			print(i)
	

usingDic(arr, target)

