import random
'''
Let's create a random array of 20 elements that lies between -50 to 50 and
sort them using "merge sort". This is a 'Divide and Conquer' technique to split
the list into half 'recursively' until we split them into single elements
and 'merge' them together in the sorted order by comparing the elements.
To learn more about merge sort visit : http://en.wikipedia.org/wiki/Merge_sort
'''


def merge_sort(random_list):
    n=len(random_list)
    if n<2:
        return
    else:
        mid=int(n/2)
        left_array=random_list[0:mid]
        right_array=random_list[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        sorted=merge(left_array,right_array,random_list)
        return sorted

def merge(left_array,right_array,sorted_array):
    i=0
    j=0
    k=0
    left_length=len(left_array)
    right_length=len(right_array)
    while i<left_length and j<right_length:
        if left_array[i]<right_array[j]:
            sorted_array[k]=left_array[i]
            i+=1
        else:
            sorted_array[k]=right_array[j]
            j+=1
        k+=1
    while i<left_length:
        sorted_array[k]=left_array[i]
        i+=1
        k+=1
    while j<right_length:
        sorted_array[k]=right_array[j]
        j+=1
        k+=1
    return sorted_array


random_list=[random.randint(-50,50) for value in range(15)]
print('unsorted array:',random_list)
ascending_sorted_array=merge_sort(random_list)
print('sorted array:', ascending_sorted_array)





