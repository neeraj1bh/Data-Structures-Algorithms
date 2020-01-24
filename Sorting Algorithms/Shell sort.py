def shell_sort(a):
	h = int(input("Enter the maximum increment (odd value) : "))
	while h >= 1:
		for i in range(h, len(a)):
			temp = a[i]
			j = i-h
			while j >= 0 and a[j] > temp:
				a[j+h] = a[j]
				j = j-h
			a[j+h] = temp
		h = h-2

############################################################

list1 = [9, 6, 8, 3, 1, 5]
shell_sort(list1)
print(list1)

list2 = [19, 266, 98, 473, 51, 5, 23, 45, 1, 99]
shell_sort(list2)
print(list2)

############################################################