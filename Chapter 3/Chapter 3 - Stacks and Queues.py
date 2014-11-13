
# coding: utf-8

## CHAPTER 3 - STACKS AND QUEUES

# In[1]:

# Imports:
import numpy as np # Array manipulations
import Queue as qu # Queue implementation
import matplotlib.pyplot as plt # To plot the maze


### PROGRAM 3.1, PAGE 129

# In[2]:

# Selection sort

def selection_sort(a,n):
    # Sort a[0] to a[n-1]
    for i in range(n):
        j = i
        # Find smallest integer in a[i] to a[n-1]
        for k in range(i+1,n):
            if a[k] < a[j]:
                j = k
        
        a[i], a[j] = a[j], a[i]


### PROGRAM 3.2, PAGE 129

# In[3]:

# Code Fragment to illustrate template instantiation
farray = [ float(j)/2 for j in range(10,0,-1) ]
intarray = [ j for j in range(25,0,-1) ]
print "Before sorting : "
print farray
print intarray

selection_sort(farray,len(farray))
selection_sort(intarray,len(intarray))

print "After sorting : "
print farray
print intarray


### PROGRAM 3.4, PAGE 131 &nbsp; & &nbsp; PROGRAM 3.5, PAGE 132

# In[4]:

# Definition of the class Bag containing integers

# The concept of capacity is not necessary in python since
# list size and memory management is done automatically by python

class Bag(object):
    def __init__(self):
        
        self._array = []
        self._top = -1
        
    def size(self):
        '''returns the number of elements in the  bag'''
        return self._top + 1
    
    def is_empty(self):
        '''return true if the bag is empty; false otherwise'''
        return size == 0
    
    def element(self):
        '''Return an element that is in the bag'''
        if self.is_empty():
            raise Exception('Bag is empty')
        else:
            return self._array[0]
        
    def push(self,elt):
        '''Add an integer to the end of the bag'''
        self._array.append(elt)
        self._top += 1
        
    def pop(self):
        '''Delete an integer from the bag'''
        self._top -= 1 
        return self._array.pop()


# In[5]:

bg = Bag()
bg.push(5)
bg.push(6)
bg.push(7)
bg.push(8)
print "Popped Item : ", bg.pop()
print "The contents of the bag : ", bg._array


# <hr>
# PROGRAM 3.6, PAGE 133 &nbsp; & &nbsp; PROGRAM 3.7, PAGE 134
# 
# Python uses [duck typing](http://en.wikipedia.org/wiki/Duck_typing), so it doesn't need special syntax to handle multiple types.
# Hence template class for Bag is not required. The above defined class Bag will suffice.
# <hr>

### ADT 3.1, PAGE 137  &nbsp; & &nbsp; PROGRAM 3.8, PAGE 138 &nbsp; & &nbsp; PROGRAM 3.9, PAGE 138

# In[6]:

# Abstract data type Stack

# NOTE: This is done just to understand the working of various methods
# Python list is very much versatile and can be readily used as a sophisticated stack
# for all practical purposes

class Stack:
    def __init__(self):
        self._stack = []
        self._top = -1
        
    def is_empty(self):
        '''If number of elements in the stack is 0, return True
           else return False'''
        return self._top == -1
    
    def top(self):
        return self._top
    
    def push(self, item):
        '''Insert item into the top of the stack'''
        
        self._stack.append(item)
        self._top += 1
        
    def pop(self):
        '''Delete the top element of the stack'''
        
        if self.is_empty():
            raise Exception('Stack is empty. Cannot delete.')
        
        self._stack.pop()
        self._top -= 1


### ADT 3.2, PAGE 140  &nbsp; &nbsp; - &nbsp; &nbsp; Program 3.2, PAGE 144 &nbsp; &nbsp; - &nbsp; &nbsp; Program 3.11 &amp; 3.12 PAGE 146 &amp; 147

# In[7]:

# Abstract data type Queue

# NOTE: Inbuilt library Queue can be used for all practical purposes.
# Again the concept of capacity is unnecessary in python, since the 
# queue containers lists are automatically managed

class Queue:
    '''Abstract Data type Queue'''
    def __init__(self):
        self._queue = []
        
    def is_empty(self):
        return len(self._queue) == 0
    
    def front(self):
        '''Return the element at the rear of the queue'''
        try:
            return self._queue[0]
        except:
            return None
        
    def rear(self):
        '''Return the element at the rear of the queue'''
        try:
            return self._queue[-1]
        except:
            return None
        
    def push(self, item):
        '''Add item to the rear of queue'''
        self._queue.append(item)
        
    def pop(self):
        '''Delete the front element of the queue'''
        if self.is_empty():
            raise Exception('Queue is empty. Cannot delete')
        else:
            self._queue.pop()


# In[8]:

# Sample I/O

a = Queue()
a.push(5)
a.push(6)
a.push(9)
a.push(8)
a.pop()
print "The contents of the queue : ", a._queue
print "The front of the queue : ", a.front()
print "The rear of the queue : ", a.rear()


### PROGRAM 3.13, PAGE 149 - PROGRAM 3.14, PAGE 150

# In[9]:

# Implementataion of stack operations.
# Here the concept of capacity is not neglected
# This allows fixed stack sizes which have many practical applications
# Again, lists can be used as stacks for all practical purposes

# Stack class inherits from class Bag

class Stack(Bag):

    def __init__(self, stack_capacity = 10):
        '''Create an empty stack whose initial capacity is stackCapacity'''
        self._stack_capacity = stack_capacity
        self._stack = []
        self._top = -1
    
    def is_empty(self):
        '''If number of elements in the stack is 0, return True
           else return False'''
        return len(self._stack)==0

    def top(self):
        if self._top != -1:
            return self._stack[self._top]
        else:
            return None

    def push(self, item):
        '''Insert item into the top of the stack'''
        # Adding to a stack, Page 138
        if self._stack_capacity == self._top + 1:
            self._stack_capacity *= 2
        self._stack.append(item)
        self._top += 1

    def pop(self):
        '''Delete the top element of the stack'''
        # Deleting from a stack, Page 138
        self._top -= 1
        if self.is_empty():
            raise Exception('Stack is empty. Cannot delete.')
        return self._stack.pop()
     
    def __str__(self):
        '''Print contents of stack'''
        
        # Based on PROGRAM 3.17, PAGE 159
        
        strval = ''
        for elt in self._stack:
            strval += str(elt)+' , '
        return strval.strip(' , ')
    
        # This is similar to overloading operator << in C++ for printing the contents of the stack
        # In python __str__ provides a method for returning the data elements as a string.

    # To iterate through the stack elements
    def __iter__(self):
        return iter(self._stack)


### PROGRAM 3.15 [ Algorithm ], PAGE 156 &nbsp; & &nbsp; PROGRAM 3.16, PAGE 158

# In[10]:

# A Simple application of Stack
# Finding a Path through a Maze. Storing the path in a stack. 
# Path is found through brute force search with backtracking

def Path(maze, mark, path_stack, m, p, startij = (0,0) ):
    '''Output a path, if any, in the maze'''
    
    # direction array [Increment required to move from current cell ]
    d_array = [(0,1), (0,-1), (-1,0), (1,0), (-1,1), (1,1), (-1,-1), (1,-1)]
    #           E,      W,      N,     S,     NE,     SE,    NW,      SW   

    si, sj = startij
    
    for di in d_array:      
        try:
            # Navigate to new cell
            i = si + di[0]
            j = sj + di[1]
            
            if (i<0) or (j<0):
                raise IndexError
                
            if (i,j) == (m,p):
                path_stack.push((i,j))
                return path_stack                
            
            if (maze[i][j] == 0) and (mark[i][j] == 0):
                mark[i][j] = 1
                path_stack.push((i,j))
                return Path(maze, mark, path_stack, m, p, (i,j) )
            
            if (maze[i][j] == 1) and (mark[i][j] == 0):
                mark[i][j] = 1
                # revert to prev valid cell if new cell address is not a part of the path
                
        except IndexError:
            continue
    try:
        return Path(maze, mark, path_stack, m, p, path_stack.pop())
    
    except Exception, e:
        print 'No Path in Maze'
        return None


# In[11]:

maze = np.array([   [ 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
                    [ 1, 0, 1, 1, 1, 1 ,1, 1, 0 ],
                    [ 1, 0, 0, 0, 1, 1 ,0, 1, 0 ],
                    [ 1, 0, 1, 0, 1, 1 ,0, 0, 0 ],
                    [ 0, 0, 1, 0, 0, 0 ,1, 0, 1 ],
                    [ 0, 1, 1, 1, 1, 1 ,1, 0, 1 ],
                    [ 0, 0, 0, 0, 0, 1 ,1, 1, 1 ],
                    [ 1, 1, 1, 1, 1, 0 ,1, 1, 0 ],
                    [ 1, 1, 1, 1, 1, 1 ,0, 0, 0 ]    ])

mark = np.zeros(maze.shape,int)

path_stack = Stack(maze.size)

path_stack.push((0,0))

print Path(maze, mark, path_stack, 8, 8)


# In[12]:

get_ipython().magic(u'matplotlib inline')
plt.figure().set_size_inches(10, 10); plt.axis('off'); plt.axis('equal')

plt.scatter(*np.where(maze == 1), s = 3000, marker = "s", c = "black", edgecolors = "w")
plt.plot(*(zip(*path_stack)), marker = "o", linestyle = "--", c = "r")

plt.show()


### PROGRAM 3.18, PAGE 162

# In[13]:

# Evaluating Postfix Expressions
def postfixvalue(a,b,expr):
    if expr == '+':
        return a + b 
    elif expr == '-':
        return a - b
    elif expr == '/':
        return a / b
    elif expr == '*':
        return a * b

def Eval(stack_e):
    '''Evaluate a Postfix expression e. It is assumed that the last token is either an operator, operand or #'''
    stack_operations = Stack()    
    while not stack_e.is_empty():
        a = stack_e.pop()
        if str(a).isdigit() != True:
            stack_operations.push(a)
        else:
            b = stack_e.pop()            
            val = postfixvalue(a,b,stack_operations.pop())
            if stack_e.is_empty():
                return val
            else:
                stack_e.push(val)
            
            
    if stack_e.is_empty() == False:
        stack_e.pop() 
    else:
        None              


# In[14]:

#Sample I/O - Not in textbook
exp = Stack()
exp.push(3)
exp.push(4)
exp.push(5)
exp.push('+')
exp.push('-')
print Eval(exp)


### PROGRAM 3.19, PAGE 165

# In[15]:

# Converting from Infix to postfix form

def isp(op):
    '''Returns the In-Stack Priority of the operator'''
    # Refer Page 160
    # Note - Unary operators are not considered they cannot be parsed by our function.
    if op in ['!']:
        return 1
    elif op in ['*','/','%']:
        return 2
    elif op in ['+','-']:
        return 3
    elif op in ['<','<=','>=','>']:
        return 4
    elif op in ['==','!=']:
        return 5
    elif op in ['&&']:
        return 6
    elif op in ['||']:
        return 7
    elif (op == '#') or (op == '('):
        return 8

def icp(op):
    '''Incoming priority of the operator'''
    if (op == '('):
        return 0
    else:
        return isp(op)
    
def Postfix(e):
    '''Output the postfix form of the infix expression '''
    stack = Stack()
    stack.push('#')
    for x in e._stack:
        if x in ['+','-','/','*']:
            # If x is an operator
            while isp(stack.top()) <= icp(x):
                print stack.pop(),
            stack.push(x)
        elif x == ')':
            # unstack untill '('
            while stack.top() != '(':
                print stack.pop(),            
                # Unstack and print it
        else:
            # If x is an operand
            print x,
    # End of expression, empty the stack
    while not stack.is_empty():
        print stack.pop(),


# In[16]:

e = Stack()
map(e.push, "A/B*C+D*E") # Push the infix expression characters one by one ( left to right ) into the e stack
Postfix(e)

