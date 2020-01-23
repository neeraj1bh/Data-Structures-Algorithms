def selection_sort(a):
	for i in range(len(a)-1):
		minIndex = i
		for j in range(i+1, len(a)):
			if a[j] < a[minIndex]:
				minIndex = j
		if i != minIndex:
			a[i], a[minIndex] = a[minIndex], a[i]

############################################################

list1 = [9, 6, 8, 3, 1, 5]
selection_sort(list1)
print(list1)

list2 = [19, 266, 98, 473, 51, 5, 23, 45, 1, 99]
selection_sort(list2)
print(list2)

############################################################