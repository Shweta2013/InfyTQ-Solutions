#PF-Assgn-43

def find_smallest_number(num):
    for value in range(1,1000):
        list_of_divisors=[]
        for num1 in range(1,value+1):
            if value%num1==0:
                list_of_divisors.append(num1)
        #print(list_of_divisors)
        if len(list_of_divisors)==num:
            return value

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)