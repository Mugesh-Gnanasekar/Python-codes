'''
In this program, we will convert a decimal number(base 10) to binary number(base 2)
'''

def D2B(num):
    dec_num=int(num)
    bin_num_reverse=[]
    while dec_num>0:
        reminder=dec_num%2
        dec_num=int(dec_num/2)
        bin_num_reverse.append(reminder)
    bin_num=[]
    bin_str=""
    for value in reversed(bin_num_reverse):
        bin_num.append(str(value))
    return bin_str.join(bin_num)

dec_num=input('Enter the Decimal number that needs to be converted to binary:')
answer=D2B(dec_num)
print (answer)