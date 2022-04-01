def bubble_sort(array):
    for item in range(len(array)):
        for j in range(0, (len(array) - item - 1)):
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])

list = [1,2,56,63,2,4,2.5,2.54]
bubble_sort(list)
print(list)