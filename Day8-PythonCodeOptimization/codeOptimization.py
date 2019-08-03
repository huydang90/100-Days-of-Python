#PYTHON CODE OPTIMIZATION

#using timer to see how fast a program runs
import time

def myfunc():
	a = 5 + 3
	b = 4 + 4 
	c = a + b
	d = c/b
	return d 

start = time.time()
myfunc()
end = time.time()
print('Time conused {} secs'.format(end-start))

def myfunc2():
	a = 5 + 3
	b = 4 + 4 
	d = (a+b)/b
	return d 

start = time.time()
myfunc()
end = time.time()
print('Time conused {} secs'.format(end-start))


#using cProfile

import cProfile

cProfile.run('2+2')

#using LineProfiler - helps define CPU bound problems
#help identify bottlenecks of CPU and RAM usage in code
from line_profiler import LineProfiler

def rock(rk): 
	print(rk)

rk = "Hello World"
profile = LineProfiler(rock(rk))

print(profile.print_stats())

#LIST AND TUPLES

#are a class of data structures called arrays: flat list of data with some intrinsic ordering 
#list are dynamic arrays 
#tuples are static arrays

#search for an item without knowing the position in a list 
my_list = [9, 18, 28, 88, 29, 61, 56, 42, 19, 95]

def linear_search(elem, array): 
	for i, item in enumerate(array): 
		if item == elem: 
			return i
		return -1
		
#this algorithm would be much faster if we sort the list first to have the smaller values on the left and bigger values on the right 
#can be achieved with __eq__ __lt__ magic functions of the object in Python 
#Sorting and Searching algorithm at the center 
#Tim-sort in Python can sort through a list in O(n) time in best case and O(nlogn) in worst case 
#=> use multiple types of sorting algorithms and heuristics to guess which will achieve best result 
#Bisect - Binary search : simplify the process of search by making it easier to add elements to a list, to find closestelements of what we are looking for 

#function to find closest element of a value => good for comparing two dataset that are similar but not identical

import bisect
import random 

def find_closest(numbers, my_val): 
	i = bisect.bisect_left(numbers, my_val)
	j = 0 
	if i == len(numbers): 
		return i - 1
	elif numbers[i] == my_val: 
		return i 
	elif i<0:
		j = i - 1
		if numbers[i] - my_val > my_val - numbers[j]: 
			return j
	return i
	
numbers = []
for i in xrange(10):
	new_number = random.randint(0,1000)
	bisect.insort(numbers, new_number)

closest_index = find_closest(numbers, 500)

#RULE OF WRITING EFFICIENT CODE: FIND RIGHT DATA STRUCTURES AND STICK WITH IT 
#SEARCHING AND SORTING ARE The most efficient algorithm for lists and tuples 
 
'''
Differences between Lists and Tuples: 
1. Lists are dynamic array and mutable 
2. Tuples are static arrays and immutable 
3. Tuples cached by python runtime => we don't have to talk to the kernel to reserve memory everytime we want to use one
4. Lists are not cached

Usage: 
Tuples: describe multiple properties of one unchanging thing 
Lists: can be used to store collection of data about completely disparate objects

To reduce overhead: 
- use packages like blist and arry 
- use numpy to transform all to the same type of data

Tuples are lightweight at the cost of immutability 
Lists are mutable at the cost of extra memory and execution 

#list as dynamic array: 
'''
numbers = [5,8,1,32,2,6]
numbers[2] = 9 
numbers.append(43)
print(len(numbers))

 #Tuples as static array: 
 t = (1,2,3,4)
 t[0] = 5
 #can concat tuples to make new tuples
 t1 = (6,7,8,9)
 print(t+t1)
 
 #Conclusion: lists and tuples = fast and low-overhead objects with intrinsic ordering
 #=> allows you to sidestep the search problem in these structures 
 #if we know the ordering beforehand => O(1) time instead of O(n) time
 #List: resizable; Tuples: fixed
 