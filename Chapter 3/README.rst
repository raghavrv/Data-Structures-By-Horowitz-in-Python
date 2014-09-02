
CHAPTER 3 - STACKS AND QUEUES
=============================

.. code:: python

    #Imports:
    import numpy as np #Array manipulations
    import Queue as qu #Queue implementation
PROGRAM 3.1, PAGE 129
---------------------

.. code:: python

    #Selection sort
    
    def SelectionSort(a,n):
        #Sort a[0] to a[n-1]
        for i in range(n):
            j = i
            #Find smallest integer in a[i] to a[n-1]
            for k in range(i+1,n):
                if a[k] < a[j]:
                    j = k
            temp = a[i]
            a.__setitem__(i,a[j])
            a.__setitem__(j,temp)
            #Swapping a[i] and a[j] using __setitem__ method
            #This emulates C++ style call by reference.
PROGRAM 3.2, PAGE 129
---------------------

.. code:: python

    #Code Fragment to illustrate template instantiation
    farray = [ float(j)/2 for j in range(100,0,-1) ]
    intarray = [ j for j in range(250,0,-1) ]
    SelectionSort(farray,len(farray))
    SelectionSort(intarray,len(intarray))
    #Sample O/P : - Not in textbook
    #print farray
    #print intarray
PROGRAM 3.3, PAGE 130
---------------------

.. code:: python

    #Function to change size of 1D array
    def ChangeSize1d(a,oldSize,newSize):
        for i in range(newSize-oldSize):
            a.append(0)
PROGRAM 3.4, PAGE 131   &   PROGRAM 3.5, PAGE 132
-------------------------------------------------

.. code:: python

    #Definition of the class Bag containing integers
    #&
    #Implementation of operations of Bag
    
    class Bag(object):
        def __init__(self,bagCapacity = 10):
            if bagCapacity < 1:
                raise Exception('Capacity must be > 0')
            self._Bag__capacity = bagCapacity
            self._Bag__array = []
            self._Bag__top = -1
        def Size(self):
            '''returns the number of elements in the  bag'''
            return self._Bag__top + 1
        def IsEmpty(self):
            '''return true if the bag is empty; false otherwise'''
            return size == 0
        def Element(self):
            '''Return an element that is in the bag'''
            if self.IsEmpty():
                raise Exception('Bag is empty')
            else:
                return self._Bag__array[0]
        def Push(self,elt):
            if self._Bag__capacity == self._Bag__top+1:
                ChangeSize1d(self._Bag__array,capacity,2*capacity)
            self._Bag__capacity *= 2
            self._Bag__array.append(elt)
            self._Bag__top += 1
        def Pop(self):
            '''Delete an integer from the bag'''
            self._Bag__array = self._Bag__array[:-1]
            self._Bag__top -= 1     
.. code:: python

    #Sample I/O - Not in textbook:
    Bg= Bag()
    Bg.Push(5)
    Bg.Push(6)
    Bg.Push(7)
    Bg.Push(8)
    Bg.Pop()
    print Bg._Bag__array

.. parsed-literal::

    [5, 6, 7]


PROGRAM 3.6, PAGE 133   &   PROGRAM 3.7, PAGE 134
-------------------------------------------------

Python uses `duck typing <http://en.wikipedia.org/wiki/Duck_typing>`__,
so it doesn't need special syntax to handle multiple types. Hence
template class for Bag is not required. The above defined class Bag will
suffice.

ADT 3.1, PAGE 137   &   PROGRAM 3.8, PAGE 138   &   PROGRAM 3.9, PAGE 138
-------------------------------------------------------------------------

.. code:: python

    #Abstract data type Stack
    class Stack:
        '''A finite ordered list with zero or more elements'''
        def __init__(self, stackCapacity = 10):
            '''Create an empty stack whose initial capacity is stackCapacity'''
            self._Stack__stackCapacity = stackCapacity
            self._Stack__stack = []
            self._Stack__top = -1
            #_Stack__<varname> is used to define (C++ Style) private variables in python.
        def IsEmpty(self):
            '''If number of elements in the stack is 0, return True
               else return False'''
            if self._Stack__top == -1:
                return True
            else:
                return False
        def Top(self):
            return self._Stack__top
        def Push(self, item):
            '''Insert item into the top of the stack'''
            #Adding to a stack, Page 138
            if self._Stack__stackCapacity == self._Stack__top + 1:
                self._Stack__stackCapacity *= 2
            self._Stack__stack.append(item)
            self._Stack__top += 1
        def Pop(self):
            '''Delete the top element of the stack'''
            #Deleting from a stack, Page 138
            if self.IsEmpty():
                raise Exception('Stack is empty. Cannot delete.')
            self._Stack__stack.pop()
            self._Stack__top -= 1
ADT 3.2, PAGE 140
-----------------

.. code:: python

    #Abstract data type Queue
    
    #Inbuilt library Queue is used. The Queue object is imported as 'qu'.
    
    class Queue:
        '''Abstract Data type Queue'''
        def __init__(self, queueCapacity = 10):
            '''Create a queue, whose initial capacity is queueCapacity'''
            self.queue = []
            self.front = -1
            self.rear = -1
            self.queueCapacity = queueCapacity
        def IsEmpty(self):
            '''If number of elements is 0 then return True else return False'''
            return len(self.queue) == 0
        def Front(self):
            '''Return the element at the rear of the queue'''
            try:
                return self.queue[self.front]
            except qu.Empty:
                return None
        def Rear(self):
            '''Return the element at the rear of the queue'''
            try:
                return self.queue[self.rear]
            except qu.Empty:
                return None
        def Push(self, item):
            '''Insert item at the rear of the queue'''
            pass
        def Pop(self):
            '''Delete the front element of the queue'''
            pass
PROGRAM 3.10, PAGE 144   &   PROGRAM 3.11, PAGE 146
---------------------------------------------------

.. code:: python

    
    #Adding to a queue, Page 144:
    def Push(self,item):
        '''Add x to the rear of queue'''
        if self.queueCapacity == self.rear+1:
            #Doubling queue capacity, Page 146
            self.queueCapacity = 2*self.queueCapacity
        self.queue.append(item)
        self.rear += 1
        if self.queueCapacity == 1:
            #for the first element added
            self.front = 0
    Queue.Push = Push 
PROGRAM 3.12, PAGE 147
----------------------

.. code:: python

    #Deleting from a queue
    def Pop(self):
        '''Delete front element from queue'''
        if self.IsEmpty():
            raise Exception('Queue is empty. Cannot delete')
        else:
            self.front += 1 
            self.queue = self.queue[1:]
            #the first element is removed from the queue.
    Queue.Pop = Pop
.. code:: python

    #Sample I/O - Not in text book:
    a = Queue(10)
    a.Push(5)
    a.Push(6)
    a.Push(9)
    a.Push(8)
    a.Pop()
    print a.queue

.. parsed-literal::

    [6, 9, 8]


PROGRAM 3.13, PAGE 149
----------------------

.. code:: python

    #Code Snippet demonstrating inheritance
    class Stack(Bag):
        '''Stack class inherits from class Bag'''
        def __init__(self, stackCapacity = 10):
            pass
        def Top(self):
            pass
        def Pop(self):
            pass
PROGRAM 3.14, PAGE 150
----------------------

.. code:: python

    #Implementataion of stack operations.
    def __init__(self, stackCapacity = 10):
        '''Create an empty stack whose initial capacity is stackCapacity'''
        self._Stack__stackCapacity = stackCapacity
        self._Stack__stack = []
        self._Stack__top = -1
        #_Stack__<varname> is used to define (C++ Style) private variables in python.
    Stack.__init__ = __init__
    def IsEmpty(self):
        '''If number of elements in the stack is 0, return True
           else return False'''
        return len(self._Stack__stack)==0
    Stack.IsEmpty = IsEmpty
    def Top(self):
        if self._Stack__top != -1:
            return self._Stack__stack[self._Stack__top]
        else:
            return None
    Stack.Top = Top
    def Push(self, item):
        '''Insert item into the top of the stack'''
        #Adding to a stack, Page 138
        if self._Stack__stackCapacity == self._Stack__top + 1:
            self._Stack__stackCapacity *= 2
        self._Stack__stack.append(item)
        self._Stack__top += 1
    Stack.Push = Push
    def Pop(self):
        '''Delete the top element of the stack'''
        #Deleting from a stack, Page 138
        self._Stack__top -= 1
        if self.IsEmpty():
            raise Exception('Stack is empty. Cannot delete.')
        return self._Stack__stack.pop()
    Stack.Pop = Pop
    
    #To print stack contents:
    def __str__(self):
        '''Print contents of stack'''
        strval = ''
        for elt in self._Stack__stack:
            strval += str(elt)+' , '
        return strval.strip(' , ')
    Stack.__str__ = __str__
    
    #To iterate through the stack elements
    def __iter__(self):
        yield list(iter(self._Stack__stack))
    Stack.__iter__ = __iter__
    
    #To convert a list element to stack
    def l2s(self,lst):
        '''Convert a list element to stack'''
PROGRAM 3.15 [ Algorithm ], PAGE 156   &   PROGRAM 3.16, PAGE 158
-----------------------------------------------------------------

.. code:: python

    #Finding a Path through a Maze
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
    
    #direction array [Increment required to move from current cell ]
    dArray = [(0,1), (0,-1), (-1,0), (1,0), (-1,1), (1,1), (-1,-1), (1,-1)]
    #           E,      W,      N,     S,     NE,     SE,    NW,      SW   
    pathStack = Stack(maze.size)
    pathStack.Push((0,0))
    def Path(m,p,startij = (0,0)):
        '''Output a path, if any, in the maze'''
        global maze
        global mark
        global dArray
        global pathStack
        (si,sj) = startij
        for di in dArray:      
            try:
                #Navigate to new cell
                i = si + di[0]
                j = sj + di[1]
                if (i<0) or (j<0):
                    raise IndexError
                if (i,j) == (m,p):
                    pathStack.Push((i,j))
                    return pathStack                
                if (maze[i][j] == 0) and (mark[i][j] == 0):
                    mark[i][j] = 1
                    pathStack.Push((i,j))
                    return Path(m,p,(i,j))
                if (maze[i][j] == 1) and (mark[i][j] == 0):
                    mark[i][j] = 1
                #revert to prev valid cell if new cell address is not a part of the path
            except IndexError:
                continue
        try:
            return Path(m,p,pathStack.Pop())
        except Exception, e:
            print 'No Path in Maze'
            return None
    print Path(8,8)


.. parsed-literal::

    (0, 0) , (0, 1) , (1, 1) , (2, 1) , (3, 1) , (4, 1) , (4, 0) , (5, 0) , (6, 0) , (6, 1) , (6, 2) , (6, 3) , (6, 4) , (7, 5) , (8, 6) , (8, 7) , (8, 8)


PROGRAM 3.17, PAGE 159
----------------------

.. code:: python

    #To print stack contents:
    def __str__(self):
        '''Print contents of stack'''
        strval = ''
        for elt in self._Stack__stack:
            strval += str(elt)+' , '
        return strval.strip(' , ')
    Stack.__str__ = __str__
    
    #This is similar to overloading operator << in C++ for printing the contents of the stack
    #In python __str__ provides a method for returning the data elements as a string.
PROGRAM 3.18, PAGE 162
----------------------

.. code:: python

    #Evaluating Postfix Expressions
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
        while not stack_e.IsEmpty():
            a = stack_e.Pop()
            if str(a).isdigit() != True:
                stack_operations.Push(a)
            else:
                b = stack_e.Pop()            
                val = postfixvalue(a,b,stack_operations.Pop())
                if stack_e.IsEmpty():
                    return val
                else:
                    stack_e.Push(val)
                
                
        if stack_e.IsEmpty() == False:
            stack_e.Pop() 
        else:
            None              
.. code:: python

    #Sample I/O - Not in textbook
    exp = Stack()
    exp.Push(3)
    exp.Push(4)
    exp.Push(5)
    exp.Push('+')
    exp.Push('-')
    print Eval(exp)

.. parsed-literal::

    6


PROGRAM 3.19, PAGE 165
----------------------

.. code:: python

    #Converting from Infix to postfix form
    def isp(op):
        '''Returns the In-Stack Priority of the operator'''
        #Refer Page 160
        #Note - Unary operators are not considered they cannot be parsed by our function.
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
        stack.Push('#')
        for x in e._Stack__stack:
            if x in ['+','-','/','*']:
                #If x is an operator
                while isp(stack.Top()) <= icp(x):
                    print stack.Pop(),
                stack.Push(x)
            elif x == ')':
                #unstack untill '('
                while stack.Top() != '(':
                    print stack.Pop(),            
                    #Unstack and print it
            else:
                #If x is an operand
                print x,
        #End of expression, empty the stack
        while not stack.IsEmpty():
            print stack.Pop(),
.. code:: python

    #Sample I/O - Not in Textbook
    e = Stack()
    e.Push('A')
    e.Push('*')
    e.Push('B')
    Postfix(e)

.. parsed-literal::

    A B * #

