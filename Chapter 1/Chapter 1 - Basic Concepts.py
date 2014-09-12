
# coding: utf-8

## CHAPTER 1 - BASIC CONCEPTS

### PROGRAM 1.1, PAGE 17

# In[1]:

#Output in C++

#Variable Declaration

n = 50
f = 20.3

#Result

print('n: '+str(n))
print('f: '+str(f))


### PROGRAM 1.2, PAGE 18

# In[2]:

#Input in C++

a = input()
b = input()

#The input values are stored in a and b


### PROGRAM 1.3, PAGE 19

# In[3]:

#File I/O in C++

try:
    outFile = open('my.out','w')
    
#Variable Declaration

    n = 50
    f = 20.3

#Result

    outFile.write('n: '+str(n)+'\n')
    outFile.write('f: '+str(f)+'\n')
    outFile.close()
    
#Error handling

except IOError:
    print 'cannot open my.out'


### PROGRAM 1.4, PAGE 19

# In[4]:

# An Example of a function

# max returns the maximum of two numbers passed to it 
# [ Note that we are overriding the default definition for max provided by the language]
def max(a,b):
    if(a>b):
        return a
    else:
        return b


### PROGRAM 1.5, PAGE 23

# In[5]:

#Throwing an exception of type char*
def div_zero(a,b,c):
    if a<=0 or b<=0 or c<=0 :
        raise Exception('All parameters should be >0')
        #raise and exception when a or b or c = 0
    return a+b*c+b/c


### PROGRAM 1.6, PAGE 24

# In[6]:

# Catching an exception.

try:
    print div_zero(2,0,4)
except Exception, e:
    print 'The parameters to DivZero were 2,0,4'
    print 'An exception has been thrown'
    print e


### PROGRAM 1.8, PAGE 27

# In[7]:

# Selection Sort

def sel_sort(a,n):
    for i in range(n):
        j = i
        for k in range(i+1,n):
            if(a[k]<a[j]):
                j = k
        a[i],a[j] = a[j],a[i]
# a[j] is the smallest no in a[i] to a[n-1]
       
# Sample I/O [ Not included in text book ]

a = [5,4,3,2,1]
sel_sort(a,len(a))
print a


### PROGRAM 1.10, PAGE 28

# In[8]:

# Binary search

def binary_search(a,x,n):
    """Search the sorted array a[0] to a[n-1] for x"""
    left = 0
    right = n-1
    while left <= right:
        # While there are more elements to search
        middle = (left + right)/2
        if x<a[middle]:
            right = middle - 1
        elif x>a[middle]:
            left = middle + 1
        else: 
            return middle
            # Returns index (starting from 0) of the element in the array.
        
    # If not found
    return -1

# Example [ not included in text]

a = [1,3,4,5,65,7,2234,23,32,342]
n = len(a)
x = 65

print binary_search(a,x,n)


### PROGRAM 1.11, PAGE 31

# In[9]:

# Recursive implemenation of binary search

def binary_search_rec(a,x,left,right):
    """Search sorted array a[left] ... a[right] for x"""
    if left<=right:
        middle = (left + right)/2
        if x<a[middle]:
            return binary_search_rec(a,x,left,middle-1)
        elif x>a[middle]:
            return binary_search_rec(a,x,middle+1,right)
        else:
            return middle
    # If the value is not found
    else:
        return -1

print binary_search_rec(a,x,0,n-1)


### PROGRAM 1.12, PAGE 32

# In[10]:

#Recursive Permutation generator

import sys
#sys contains the output stream stdout

#Generate all permutations of a[k] .... a[m]
def permutations(a,k,m):
    if k == m:
        for i in range (m+1):
            sys.stdout.write(str(a[i])+' ')
        sys.stdout.write('\n')
    else:
        #a[k:m] has more than one permutation. Generate these recursively
        for i in range (k,m+1):
                a[k],a[i] = a[i],a[k]
                permutations(a,k+1,m)
                a[k],a[i] = a[i],a[k]
                
#Sample I/O [Not included in textbook]
a = [1,5,2]
permutations(a,0,len(a)-1)


### PROGRAM 1.13, PAGE 35

# In[11]:

# Compute the product of the elements a[0:n-1]

import operator

def accumulate(a, start, end, initialValue, op):
    """returns op(sum or product or difference etc ) of values"""

    #since python does not have mechanism for pointer implementations
    #array implementation of accumulate is done
    #start -> index of first element of array a
    #end -> index of last element of array a

    for e in range(start,end+1):
        initialValue = op(initialValue,a[e])
    return initialValue

# Returns the product of numbers a[0] ... a[n-1]
def product(a,n):
    initVal = 1
    return accumulate(a,0,n-1,initVal,operator.mul)


### PROGRAM 1.14, PAGE 36

# In[12]:

# Permutations using library functions

import itertools
# contains support for permutations() which is python equivalent of 
# C++ STL function next_permutation

class next_permutation_generator(object):
    def __init__(self, a,m ):
        self.permutation_iterator = itertools.permutations("".join(c for c in a[:m]))
    def __call__(self, a,m):
        '''Returns True if next permutation of a exists'''
        try:
            del a[:]
            for c in next(self.permutation_iterator):
                a.append(c)
            return True
        except StopIteration:
            return False

def Permutations(a,m):
    '''Print all permutations of a[0:m]'''
    a= list(a)
    # converts string a to list a to facilitate inplace computation
    # so as to make next_permutation functionally similar to 
    # call by reference function in C++
    next_permutation = next_permutation_generator(a,m) 

    while next_permutation(a,m):
        print "".join(c for c in a)
        
#sample I/O  [ Not included in textbook]
Permutations('ABCDEF',3)


### PROGRAM 1.6, PAGE 38

# In[13]:

#Function to compute a+b+b*c+(a+b-c)/(a+b)+4.0

def abc(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    return a+b+b*c+(a+b-c)/(a+b)+4.0


### PROGRAM 1.17, PAGE 39

# In[14]:

# Iterative function for sum
# NOTE that this overrides the sum function of python

def sum(a,n):
    s = 0
    for i in range(n):
        s += a[i]
    return s


### PROGRAM 1.18, PAGE 39

# In[15]:

# Recursive function for sum
def rsum(a,n):
    if n<=0:
        return 0
    else:
        return rsum(a,n-1)+a[n-1]


### PROGRAM 1.19, PAGE 44

# In[16]:

# Program 1.17 with count statements added (to compute time complexity)
# Note that this overrides the default definition of sum in python

count = 0
def sum(a,n):
    s = 0
    global count
    count += 1
    for i in range(n):
        count += 1    #for for loop
        s += a[i]
        count += 1    #for assignment
    count += 1        #for last time of for
    count += 1        #for return
    return s


### PROGRAM 1.20, PAGE 44

# In[17]:

#Simplified version of Program 1.19

count = 0
def sum(a,n):
    s =0
    global count
    for i in range(n):
        s += a[i]
        count +=2
    count +=3
    return s


### PROGRAM 1.21, PAGE 45

# In[18]:

#Program 1.18 with count statements added
count = 0
def rsum(a,n):
    if n<=0:
        global count
        count += 1     # for return
        return 0
    else:
        count += 1     # for return
        return rsum(a,n-1)+a[n-1]


### PROGRAM 1.22, PAGE 46

# In[19]:

#Matrix Addition
import numpy as np
def add(a,b,c,m,n):
    for i in range(m):
        c[i] = [ a[i][j]+b[i][j] for j in range(n)]
        
#Sample I/O - [Not given in textbook]

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[4,5,6],[7,8,9]]
c = [[],[],[]]
add(a,b,c,3,3)
c = np.array(c,float)
print c


### PROGRAM 1.23, PAGE 47

# In[20]:

#Matrix addition with counting statements

def matrix_add(a,b,c,m,n):
    global count
    count += 1
    #for for loop i
    for i in range(m):
        count += 1    #for for loop j
        s = [a[i,j]+b[i,j] for j in range(n)]
        c[i] = s
        count += 1    #for assignment
        count += 1 #for last time for j
    count += 1 #for last time for i    


### PROGRAM 1.24, PAGE 47

# In[21]:

#Simplified program with counting only

def matrix_add_count_only(a,b,c,m,n):
    global count
    for i in range(m):
        for j in range(n):
            count += 2
        count += 2
    count += 1


### PROGRAM 1.25, PAGE 50

# In[22]:

# Fibonacci Number
def fibonacci(n):
    """
    Compute the Fibonacci number Fn for the given n.
    Refer : http://en.wikipedia.org/wiki/Fibonacci_number
    """
    if n<= 1:
        print n   #F0 = 0 and F1 = 1
    else:
        #Compute Fn
        fnm2 = 0
        fnm1 = 1
        for i in range(2,n+1):
            fn = fnm1 + fnm2
            fnm2 = fnm1
            fnm1 = fn
        print fn
        
# Sample I/O [Not in textbook]
fibonacci(7)


### PROGRAM 1.26, PAGE 58

# In[23]:

#Magic Square

def magic_square(n):
    '''Create a magic square of size n, n is odd'''
    max_size = 51
    
    # Check if n is within range
    if ( n > max_size ) or ( n < 1 ):
        raise Exception('Error!..n out of range')
    elif (n%2) == 0:
        raise Exception('Error!..n is even')
    
    # n is odd. Coxeter's rule can be applied
    square = np.zeros((n,n))
    square[0][(n-1)/2] = 1
    # middle row of 1st element
            
    # i and j are current positions
    key = 2
    i = 0
    j = (n-1)/2
    nsquared = n*n
    while key <= nsquared:
        #Move up and left
        k = (n-1) if (i-1)<0 else (i-1)
        l = (n-1) if (j-1)<0 else (j-1)
        if square[k][l] != 0 :    #if square occupied, move down
            i = (i+1)%n
        else:
            #Square is unoccupied
            i = k
            j = l
        square[i][j] = key
        key +=  1
    print 'magic square of size', n
    print square

# Sample I/O [ Not in textbook ]
magic_square(5)


### PROGRAM 1.27, PAGE 62

# In[24]:

# Sequental Search
i = 0
def sequential_search(a,n,x):
    global i
    for i in range(n):
        if(a[i] == x):
            break
    if(i==n):
        return -1
    else:
        return i

# Sample I/O - [ Not in Textbook]
a = [1,3,4,5,65,7,2234,23,32,342]
print sequential_search(a,len(a),32)


### PROGRAM 1.28, PAGE 63

# In[25]:

# Program to time Program 1.27

# For getting the current processor time
import time as t

def time_search():                
    a = range(1,1001)
    n = [10*j for j in range(10)] + [100*j+100 for j in range(10)]
    print 'n \ttime'
    print '==========================='
    for j in range(20):
        # Obtain Computing times
        start = t.clock()                      #Start timer
        k = sequential_search(a,n[j],0)   #Unsuccessfull search
        stop = t.clock()                       #Stop timer
        run_time = (stop - start)
        print n[j],'\t',run_time
    print 'Times are in hundredths of a second'

#Sample I/O not included in text book:
time_search()

#Returns all zeros since accuracy of clock is 1/100 of a second


### PROGRAM 1.29, PAGE 65

# In[26]:

# Timing Program - (Using repetitive testing)

# For getting the current processor time
import time as t

def time_search():                
    a = range(1,1001)
    n = [10*j for j in range(10)] + [100*j+100 for j in range(10)]
    r = [300000,300000,200000,200000,100000,100000,100000,80000,80000]
    r += [50000,50000,25000,15000,15000,10000,7500,7000,6000,5000,5000]
    
    print 'n \ttotalTime \trunTime'
    print "==========================================="
    for j in range(20):
        #Obtain Computing times
        start = t.clock()                      #Start timer
        for b in range (r[j]+1):
            k = sequential_search(a,n[j],0)   #Unsuccessfull search
        stop = t.clock()                       #Stop timer
        totalTime = (stop - start)*1000
        runTime = float(totalTime)/float(r[j])
        print str(n[j])+'\t'+str(totalTime)+'\t\t'+str(runTime)
    print '\nTimes are in hundredths of a second'

# Sample I/O not included in text book:
time_search()

# Returns all zeros since accuracy of clock is 1/100 of a second

