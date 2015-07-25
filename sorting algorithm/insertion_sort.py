import random
'''
Let's create a random array of 20 elements that lies between -50 to 50 and
sort them using "insertion sort'
To learn more about insertion sort visit : http://en.wikipedia.org/wiki/Insertion_sort
'''


def insertion_sort_asc(random_numbers):
    for i in range(1,len(random_numbers)):
        j=i
        while j>0 and random_numbers[j]<random_numbers[j-1]:
            random_numbers[j],random_numbers[j-1]=random_numbers[j-1],random_numbers[j]
            j-=1
    return random_numbers

def insertion_sort_des(random_numbers):
    for i in range(1,len(random_numbers)):
        j=i
        while j>0 and random_numbers[j]>random_numbers[j-1]:
            random_numbers[j],random_numbers[j-1]=random_numbers[j-1],random_numbers[j]
            j-=1
    return random_numbers



random_numbers=[random.randint(-50,50) for value in range(20)]
print('unsorted array:',random_numbers)
ascending_sorted_array=insertion_sort_asc(random_numbers)
print('Ascending_sorted array:', ascending_sorted_array)
descending_sorted_array=insertion_sort_des(random_numbers)
print('Descending_sorted array:', descending_sorted_array)




