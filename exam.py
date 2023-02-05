'''
#Making Decisions and repeating instructions answers
#edit the code from the lines below
i = int(input("Enter number : "))
for x in range(-i,0):
      print(x)
      
'''


'''
# Hint: pattern contains 5 rows
row = int(input())
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1,row+1,1):
    # Run inner loop i+1 times
    for j in range(i):
        j=j+1
        print(j, end=' ')
    # empty line after each row
    print("")
    
'''

'''
num = int(input("Enter your numbers:" ))
count = 0
while num!=0 :
  num//=10
  count=count+1
print("Total digits are:", count)

OR

number=str(num)
print(len(num))

'''

'''  
n = int(input())
for i in range(1,11):
    print(n*i)

'''


'''
l = input("Input a letter of the alphabet: ")
if l in('a','e','i','o','u'):
    print(l," is a vowel.")
else:
    print(l," is a consonant.")

'''

'''
rows = int(input())
for i in range(0, rows):
    for j in range(0, i + 1):
        print("@", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("@", end=' ')
    print("\r")
'''

'''
h_age = int(input("Input a dog's age in human years: \n"))
#Add code here
if h_age<0:
    print("Age must be positive number.")
elif h_age<=2:
    d_age=h_age*10.5
else:
    d_age=21+(h_age-2)*4


print("The dog's age in dog's years is", d_age)
'''


'''
# first two numbers
num1 = int(input()) 
num2 = int(input())

print("Fibonacci sequence:")
#add code here
for i in range(10):
    if not(num1>987):
        print(num1,end="  ")
        res=num1+num2
        num1=num2
        num2=res
'''

'''
#Functions

# feel free to use these dictionaries in your solution!
str_to_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
num_to_str = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

def add_str_nums(num_1, num_2):
    if num_1 in str_to_num:
        val_1=str_to_num[num_1]
    else:
        val_1=0
    if num_2 in str_to_num:
        val_2=str_to_num[num_2]
    else:
        val_2=0
        
    sum_val=val_1+val_2
    
    if sum_val in num_to_str:
        return num_to_str[sum_val]
    else:
        return "greater than ten" # change this
        
    
	# YOUR CODE HERE
	

# Input handling (do not edit)
parts = input().split(" ")
print(add_str_nums(parts[0], parts[1]))
'''
'''
def a_vs_b(a,b):
	# your code here
	if a>b:
	    return "a is greater than b"
	elif a < b:
	    return "a is less than b" 
	else:
	     return "a is equal to b"

# Input handling, do not modify!
input_parts = input().split(" ")
a = int(input_parts[0])
b = int(input_parts[1])
print(a_vs_b(a, b))
'''
'''
num1 = int(input("Enter start number"))
num2 = int(input("Enter end number"))
num3 = int(input("Enter step number"))
print(list(range(num1,num2,num3)))
'''

'''
def int_to_string(num):
    # Your code here
    if num == 0:
        return "zero"
    elif num==1:
        return "one"
    elif num==2:
        return "two"
    elif num==3:
        return "three"
    elif num==4:
        return "four"
    elif num==5:
        return "five"
    elif num==6:
        return "six"
    elif num==7:
        return "seven"
    elif num==8:
        return "eight"
    elif num==9:
        return "nine"
    else:
        return ""

# Input handling, do not modify!
num = int(input())
print(int_to_string(num))
'''

'''
def zero_to_n(n):
	# Your code here
	for x in range(0,n+1,1):
	    print(x)

# Input handling, do not modify!
n = int(input())
zero_to_n(n)

'''

'''
name = input("Name:\n")
age = int(input("Age:\n"))
def demo(name, age):
    # print value
    print(name, age)

# call function
demo(name, age)
'''
'''
def display_student(name, age):
    print(name, age)



name = input("Enter name:")
age = int(input(""))


showStudent = display_student(name,age)

'''
'''

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)
'''

'''

def max_of_three( x, y, z ):
    if x > y and x > z:
        return x
    elif y>z and y>z:
        return y
    else:
        return z
        
    
    
num1 = int(input("Please enter num1"))
num2 = int(input("Please enter num2"))
num3 = int(input("Please enter num3"))
print("The max of the three numbers is:",max_of_three(num1, num2, num3))
'''

#Progess Exam Fibonacci
'''
num1 = int(input())
num2 = int(input())
next = num1 + num2
print(next)
'''

'''
Fibonacci_list = []
# first two numbers
num1 = 0
num2 = 1
Fibonacci_list.append(num1)
Fibonacci_list.append(num2)
num3=int(input())
for i in range(num3-2):
    res=num1+num2
    Fibonacci_list.append(res)
    num1=num2
    num2=res
print(Fibonacci_list)
    
'''

'''
Fibonacci_list = []
# first two numbers
num1 = 0
num2 = 1
num3 = int(input())
Fibonacci_list.append(num1)  
Fibonacci_list.append(num2)  
def Fibonacci(num1,num2,num3):
    for i in range(num3-2):
      res=num1+num2
      Fibonacci_list.append(res)
      num1=num2
      num2=res
    print(Fibonacci_list)
    
Fibonacci(num1,num2,num3)


'''

'''
num1 = int(input())
num2 = int(input())

print("Fibonacci sequence:")
for i in range(10):
    if not(num1>987):
        print(num1, end="  ")
        res=num1+num2
        num1=num2
        num2=res


'''

#Data Structures
'''
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concat = input("Concatenate the lists: Y/N?\n")
res=[x+y for x in list1 for y in list2]
print(res)
'''

'''
#tuples

tuple1 = (11, [22, 33], 44, 55)
new_num = int(input("Enter 222:\n"))

tuple1[1][0]=new_num
print(tuple1)

'''

'''
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
index1 = int(input("Enter index 1 of the slice:\n"))
index2 = int(input("Enter index 2 of the slice:\n"))

print(tuple1[index1][index2])


'''
'''
tuple1 = (11, 22)
tuple2 = (99, 88)
#add your code here
run = input("Swap tuples:Y/N?")
tuple1,tuple2=tuple2,tuple1
print(tuple2)
print(tuple1)
'''

'''
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements=list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements=list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)


print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

'''

'''
tuple1 = (10, 20, 30, 40, 50)
indexing = int(input("Enter index:"))
tuple1 = tuple1[::indexing]
print(tuple1)

'''

'''
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
#add your code here
element=sample_list.pop(4)
print("List After removing element at index 4 ",sample_list)

#add your code here
sample_list.insert(2,element)
print("List after Adding element at index 2 ",sample_list)

#add your code here
sample_list.append(element)
print("List after Adding element at last ",sample_list)

'''
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
number=int(input("Enter a number to add list(7000):"))
list1[2][2].append(number)
print(list1)
'''

'''
tuple1 = (11, 22, 33, 44, 55, 66)
slice_index1 = int(input("Please enter slice index 1:"))
slice_index2 = int(input("Please enter slice index 2:"))
tuple2=tuple1[3:-1]
print(tuple2)


'''
'''
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

print("Original list", sample_list)

user= input("Create new tuple:Y/N?")

sample_list = list(set(sample_list))
print("unique list", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))


'''

#DATA STRCUTER QUIZ
'''
def sum(numbers):
    total=0
    for x in numbers:
        total += x
    return total
    
    
    
print(sum((8,2,3,0,7)))

'''

'''
def multiply(numbers):
    total=1
    for x in numbers:
     total *=x
    return total
 print(multiply((8,2,3,-1,7)))
'''

'''
def isPalindrome(string):
    left_pos=0
    right_pos=len(string)-1
    
    while right_pos >= left_pos:
        if not string[left_pos]==string[right_pos]:
            return False
        left_pos+=1
        right_pos-=1
    return True
    
    
    
    
word = input("Please type in a word to test the program:")    
print(isPalindrome(word))


'''

'''
#create a tuple
tuplex = 4, 8, 3 
print(tuplex)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1+n2+n3) 
#the number of variables must be equal to the number of items of the tuple
n1, n2, n3, n4=tuplex


'''

'''
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1,2,3,3,3,3,4,5]))

'''

#Progress exam 4
