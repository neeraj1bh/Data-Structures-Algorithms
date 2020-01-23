def bubble_sort(a):
	for i in range(len(a)-1, 0, -1):
		for j in range(i):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]

############################################################

list1 = [9, 6, 8, 3, 1, 5, 4, 98, 55]
bubble_sort(list1)
print(list1)

list2 = [19, 266, 98, 473, 51, 5, 23, 45, 1, 99, 66, 87]
bubble_sort(list2)
print(list2)

############################################################