__author__ = 'Mugesh'
'''
This is a basic bubble sort algorithm which can be used to arrange numbers or strings in
any particular order like ascending or descending order. The main thing about bubble sort is
we sort by comparing each value with other values and move through the list. Hence this makes
this algorithm slower when the data to sort is large.

'''

def ascending(list):

    length = len(list)
    for i in range(length-1):
        for j in range(length-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
            else:
                continue

    return list

def descending(list):
    length = len(list)
    for i in range(length-1):
        for j in range(length-1):
            if list[j]<list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
            else:
                continue

    return list

list_str=input('Enter the list that needs to be sorted: ')
split_list=list_str.split(',')
int_list=[]
for value in split_list:
    int_list.append(int(value))

option=input('Enter "a" for ascending order or "d" for descending order: ')
if option=='a':
    sorted=ascending(int_list)
    print(sorted)
elif option=='d':
    sorted=descending(int_list)
    print(sorted)