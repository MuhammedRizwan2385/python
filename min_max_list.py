#read n numbers into a list and create a function min_max() that will return smallest and largest among list numbers
def min_max(a):
    a.sort()
    smallest_number=a[0]
    largest_number=a[-1]
    return smallest_number,largest_number
n=int(input("Enter the no of terms:"))
a=[]
for i in range(n):
    num=int(input(f"Enter the element {i+1}: "))
    a.append(num)
small,large=min_max(a)
print(f"Smallest number:{small} largest number:{large}")
