import random
'''
Let's create a random array of 20 elements that lies between -50 to 50 and
sort them using "Quick sort". In this technique, we select a pivot element first
and then move all elements less then the pivot to left of it and all greater elements
to the right of it.Then sort the left segment separately and right segment separately.
To learn more about quick sort visit : https://en.wikipedia.org/wiki/Quicksort
'''

def Quick_sort(random_list,start,end):
    if start<end:
        partition_index=Partition(random_list,start,end)
        Quick_sort(random_list,start,partition_index-1)
        Quick_sort(random_list,partition_index+1,end)
        return random_list


def Partition(random_list,start,end):
    pivot=random_list[end]
    pIndex=start
    for i in range(start,end):
        if random_list[i]<=pivot:
            random_list[i],random_list[pIndex]=random_list[pIndex],random_list[i]
            pIndex+=1
    random_list[pIndex],random_list[end]=random_list[end],random_list[pIndex]
    return pIndex


random_list=[random.randint(-50,50) for value in range(6)]
print('unsorted array:',random_list)
start=0
end=5
ascending_sorted_array=Quick_sort(random_list,start,end)
print('sorted array:', ascending_sorted_array)





