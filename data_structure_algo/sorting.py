"""
all sorting algorithms
"""
## merge sort -- recursion
def merge_sort(arr):
	if not arr: return []
	l, r = 0, len(arr)
	m = (l+r)//2
	if l >= r-1:
		return [arr[l]]
	l = merge_sort(arr[l:m])
	r = merge_sort(arr[m:r])
	return merge(l, r)

def merge(a1, a2):
	"""
	params: 
		a1, a2: two sorted arrays and merge into one
	returns:
		merged array
	"""
	i, j = 0, 0
	ans = []
	l1, l2 = len(a1), len(a2)
	while i < l1 and j < l2:
		if a1[i] < a2[j]:
			ans.append(a1[i])
			i += 1
		else:
			ans.append(a2[j])
			j += 1
	ans.extend(a1[i:] or a2[j:])
	return ans

## merge sort -- iteration
def merge_sort1(arr):
	if not arr: return []
	step = 1
	l = len(arr)
	while step <= l:
		tmp = []
		i = 0
		while i < l:
			tmp.extend(merge(arr[i:i+step], arr[i+step:i+2*step]))
			i+= 2*step
		step = step*2
		arr = tmp
	return arr

## quick sort -- recursion
def partition(arr, start, end):
	pivot_index = start
	while start < end:
		while start < len(arr) and arr[start] <= arr[pivot_index]:
			start += 1
		while end > -1 and arr[end] > arr[pivot_index]:
			end -= 1
		if start < end:
			arr[start], arr[end] = arr[end], arr[start]
	arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
	return end

def quick_sort(arr, start, end):
	if not arr: return []
	if start < end:
		p = partition(arr,start,end)
		quick_sort(arr, start, p-1)
		quick_sort(arr, p+1, end)





## test
arr1 = []
arr2 = [1]
arr3 = [6,4,2,4,1,2,0]
arr4 = [3,1,2,-1]
merge_sort(arr1)
merge_sort(arr2)
merge_sort(arr3)
merge_sort(arr4)


merge_sort1(arr1)
merge_sort1(arr2)
merge_sort1(arr3)
merge_sort1(arr4)

quick_sort(arr1, 0, len(arr1)-1)
quick_sort(arr2, 0, len(arr2)-1)
quick_sort(arr3, 0, len(arr3)-1)
quick_sort(arr4, 0, len(arr4)-1)
