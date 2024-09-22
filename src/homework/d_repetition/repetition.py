
def get_factorial(num):

    num2=1

    for i in range (1,num+1):
        num2=num2*i
     #   print(i)
    return num2

def sum_odd_numbers(num):
    i=1
    sum=0
    while (i<=num):
        sum=sum+i
        i+=2
    return sum
