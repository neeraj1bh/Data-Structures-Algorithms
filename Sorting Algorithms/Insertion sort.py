def insertion_sort(a):
	for i in range(1, len(a)):
		temp = a[i]
		j = i-1
		while j>=0 and a[j]>temp:
			a[j+1] = a[j]
			j = j-1
		a[j+1] = temp

############################################################

list1 = [9, 6, 8, 3, 1, 5, 12, 36, 95, 4, 10]
insertion_sort(list1)
print(list1)

list2 = [19, 266, 98, 473, 51, 5, 23, 45, 1, 99, 96, 69]
insertion_sort(list2)
print(list2)

############################################################