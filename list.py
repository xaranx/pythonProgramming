list = ["Sunday", "Monday", "Tusday", "wednesday", "Thirsday", "Friday", "Saturday"]

#for day in list:
#    print(day)
#print[day for day in list]


# program to sum all the items in a list
#items = [2, 5, 6, 9, 4]
#sum = 0
#for i in items:
#    sum += i
#print("sum = {}".format(sum))
#[sum := sum + i for i in items]
#print(sum)

# ---- program to sum all the items in a list---- 
print("---- program to sum all the items in a list----")
def sum_list(items):
    sum = 0
    [sum := sum + i for i in items ]
    return sum 
print(sum_list([2, 5, 6, 9, 4, 7]))

print("---- program to mul all the items in a list----")

def mul_list(items):
    mul = 1
    [mul := mul * i for i in items ]
    return mul
print(mul_list([1, 4, 6]))

print("---program to get the largest number from a list ---")

def maxnum(items):
    max = items[0]
    for i in items:
        if (max < i):
            max = i
    return max
print(maxnum([5, 7, 0, 1, 11]))

