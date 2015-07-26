'''
In this program, we will convert a binary number (base 2) to a decimal number
(base 10). We will do in two different ways and the latter being very simple!
'''

def B2D_1(bin_num):
    bin_list=bin_num.strip()
    bin_int=[]
    for value in bin_list:
        bin_int.append(int(value))
    decimal_value=0
    i=0
    j=len(bin_int)-1
    max_power=len(bin_int)
    while j>=0 and i<max_power:
        decimal_value+=bin_int[j]*pow(2,i)
        j-=1
        i+=1
    return decimal_value

def B2D_2(bin_num):
    bin_num_int=int(bin_num)
    decimal_value=0
    power=0
    while bin_num_int>0:
        decimal_value += (bin_num_int%10)*2**power
        bin_num_int//=10
        power+=1
    return decimal_value



bin_num=input('Enter the binary number that needs to be converted to decimal:')
answer_1=B2D_1(bin_num)
print (answer_1)
answer_2=B2D_2(bin_num)
print (answer_2)
