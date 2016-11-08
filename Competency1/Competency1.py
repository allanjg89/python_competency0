import math 

###########################################################
#                  STRING PRACTICE                        #
#         Refer to CodingBat.com 's String Basics         #
###########################################################
def greet(name):
	# Given a string name, return a greeting of the form "Hello, Name!"
	#str1('Bob')-> 'Hello Bob!'
	#str1('Alice')-> 'Hello Alice!'
	#str1('X')-> 'Hello X!'
	Greeting = "Hello " + name + "!"
	
	return Greeting

def abba(a,b):
	# Given two strings, a and b, return the result of putting them in 
	# the order of abba.  e.g. "Hi" and "Bye" returns "HiByeByeHi"	

	return a+b+b+a

def slice_us(out,word):
	# Given an "out" string length of 4, such as "<<>>", and a word
	# return a new string (c)  where the word is in the middle of the out
	# string.  e.g. slice_us("<<>>", "word") -> "<<word>>"

	return out[0:2]+word+out[2:]

def duplicate(s,n):
	# Given a string s and a number n, return a new string made of
	# n copies of the last 2 chars in the original str. (hint: slicing)
	# e.g. duplicate("word", 4) -> "rdrdrdrd"
    last2 = s[-2:]
    return_word = ""
    for x in range(0,n):
        return_word+=last2
    return return_word

def shortlongshort(s1,s2):
	# Given 2 strings, return a new string in the form of shortlongshort
	# use len(s) to figure out the length of a str
    if len(s1)<len(s2):
        return  s1+s2+s1
    else:
        return s2+s1+s2 
	
	

#########################################################
#                    INTEGER PRACTICE                   #
#########################################################
def adding(a,b):
	# return the sum of the two values
	# unless the values are the same, then double their sum
    if a != b:
        return a+b
    else:
        return 2*(a+b)

def abs_dif(n):
	# given an int n, return the absolute value of the difference between n and 21
	# double it if n is over 21
	# use abs(calculation) to give you the absolute value
    if n>21:
        return abs(n-21)*2
    else:
        return abs(n-21)

def tens(a,b):
	# given 2 ints, return True if one of them is 10, or if their sum is 10
	# else return false
    if a==10 or b==10 or a+b==10:
        return True 
    else:
        return False

def hundreds(n):
	# given an int n, return True if it is within 10 of 100
	# note: abs(num) computes the absolute value of a number
    if abs(100-n)<=10:
        return True
    else:
        return False 

def negatives(a,b,negative):
	# given 2 int values, return True if one is negative and one is positive
	# Except if the paramater "negative" is True, then return True only if both are negative
	# otherwise return false
    if negative:
        if a<0 and b<0:
            return True
        else:
            return False
    else:
        if (a<0 and b>0) or (a>0 and b<0):
            return True
        else:
            return False


	

#######################################################
#                     LIST PRACTICE                   #
#######################################################
def sixes(a):
	# given a list of integers a, return True if 6 appears as either
	# the first or last element.  The array length will be one or more
	# hint: use a for loop
    if a[0] == 6 or a[1]==6:
        return True
		

def same_length(a):
	# given an array of ints, return True if the array is length 1 or more
	# and the first element and the last element are the same value
	# list2([1,2,3,4]) -> False
	# list2([1,2,3,1]) -> True
    if len(a)>1 and a[0] == a[-1]:
        return True
    else:
        return False

def sum_list(l):
	# given an array of integers, return the sum of those integers
	# there is a built in function that does this already, bonus points if you use it
	# type "dir(__builtins__)" in the python console to view a list of builtin functions
	
	return sum(l)

def rotate_slice(l):
	# given a list l, rotate it left by 2 spaces
	# [1,2,3,4] -> [3,4,1,2]
	# use slicing, do not create a new list
    temp = l[-2:]
    l[2:] = l[0:len(1)-2]
    l[0:2] = temp
    return l

def pop_append(l):
	# give a list l of integers, do the following:
	# 1. remove the last 2 items from the list (use l.pop())
	# 2. append the product of the popped values (use l.append(value))
	# 3. append the sum of the first 2 items in the list.
    a = l.pop()
    b = l.pop()
    l.append(a*b)
    l.append(l[0]+l[1])
    return l


#########################################
#           BOOLEAN PRACTICE            #
#########################################
def basic_bool(a, b, c):
	#write "if" statements that check if a,b,c are true or false
	#note: do not do a==False or a==True
	#return the number of True's
    print("a is true") if a else print("a is false")
    print("b is true") if b else print("b is false")
    print("c is true") if c else print("c is false")

def multi_bool(a,b):
	#write an "if" statement that checks if the product of a and b
	# is greater than 0 if so return True, else return False
    if a*b>0:
        return True
    else:
        return False

def iter_bool(a):
	#a is a list of integers, using a for loop, iterate through a to find 
	#all instances of the number 7.  If a 6 appears, break out of the for loop.
	#if the number of 7's found is 0, return the number 1337
    seven_is_here = False
    for value in a:
        if x == 7:
            seven_is_here = True
        if x == 6:
            break
    if not seven_is_here:
        return 1337
    else:
        return 0


def complex_bool_one(a,b,c):
	# write a SINGLE return statement, an no other lines of code
	# return true if a is greater than b and c
	return True if (a>b and a>c) else False

def complex_bool_two(a,b,c):
	# write a single return statment: return true if -
		#1- one of a OR b is close to c (within 1 number)
		#2- one of a OR b is far from the other two (>= 2 away)
		#note: use abs() to find the absolute value.
	return True if ((abs(a-c)<=1 ^ abs(b-c)<=1) or (abs(a-c)>=2 ^ abs(b-c)>=2)) else False

	
##################################################
#              LOOPING AND ITERATION             #
##################################################
def count_for(l):
	# given a list of strings (l), iterate through each item using a counter
	# if the item begins with "xkcd", strip off "xkcd" from the beginning
	# and replace it with "CAD".  Return the changed list.
	# Note: Do not create a second list.  Operate on the exiting one.
    index = 0
    for str in l:
        if str[0:4] == "xkcd":
            str = "CAD"+str[4:]
        l[index] = str
        index += 1

    return l

def iter_for(l):
	# given a list of integers (l), iterate through each item
	# if the int is even, add it to even_sum
	# if the int is odd, add it to odd_sum
	# After summing all the numbers, return the product of even_sum and odd_sum
    even_sum = 0
    odd_sum = 0
    product = 0
    for int in l:
        if int % 2 == 0:
            even_sum += int
        else:
            odd_sum += int
    
    product = even_sum*odd_sum
    return product

def pop_while(l):
	# Given a list of integers (l), use a while loop that tests if l evalutes to True (not empty)
	# If l is not empty, use l.pop() to add the numbers in the list to m
	# return l and m
    m = []
    while len(l)>0:
        m.append(l.pop())
    
    return l,m



###############################################
#               FUNCTIONS!                    #
###############################################

def functions_one():
	# write a function named my_first_function
	# have it accept no parameters, and return True
	# use "def" to define a function, just like this function!
	# also makes sure you define it above this one
	f = my_first_function
	return f

def my_first_function():
    return True

def functions2():
	# write a function named my_second_function
	# have it return the product of a,b
	f = my_second_function
	return f

def my_second_function(a,b):
    return a*b

print(greet("Allan"))
print(abba("hi","bye"))
print(slice_us("<<>>", "word"))
print(duplicate("word", 4))
print(shortlongshort("aa","b"))