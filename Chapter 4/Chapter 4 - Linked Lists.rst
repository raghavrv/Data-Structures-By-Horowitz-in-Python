
PROGRAM 4.1, PAGE 179
---------------------

.. code:: python

    #Composite Classes
    
    #Python does not support friend funcitons hence 2 classes one for the node and one for the class are declared.
    
    class ThreeLetterNode:
        data = None
        link = None
    class ThreeLetterChain:
        '''A linked list of 3 letter strings'''
        first = None
PROGRAM 4.2, PAGE 180
---------------------

.. code:: python

    #Nested Classes
    class ThreeLetterChain:
        class ThreeLetterNode:
            data = None
            link = None
        first = None
PROGRAM 4.3, PAGE 182
---------------------

.. code:: python

    #Creating a two-node list
    class ChainNode:
        def __init__(self, data, link = None):
            self.data = data
            self.link = link
    class Chain:
        def __init__(self, first):
            self.first = first
    def Create2(self):
        #Create and set fields of second node
        self.second = ChainNode(20,None)
        
        #Create and set fields of first node
        self.first = ChainNode(10,second)
    Chain.Create2 = Create2
PROGRAM 4.4, PAGE 182
---------------------

.. code:: python

    #Inserting a Node
    def Insert50(self,x):
        if self.first is not None:
            #Insert after x
            x.link = ChainNode(50,x.link)
        else:
            #Insert into empty list
            first = ChainNode(50)
    Chain.Insert50 = Insert50
PROGRAM 4.5, PAGE 183
---------------------

.. code:: python

    #Deleting a node
    def Delete(self,x,y):
        if x == self.first:
            self.first = self.first.link
        else:
            y.link = x.link
    Chain.Delete = Delete
PROGRAM 4.6, PAGE 186
---------------------

Python uses `duck typing <http://en.wikipedia.org/wiki/Duck_typing>`__,
so it doesn't need special syntax to handle multiple types. Hence
template class for Chains is not possible in Python.

PROGRAM 4.7, PAGE 187
---------------------

.. code:: python

    #Pseudo code for computing maximum element
    
    def Max(C):
        return max(C)
PROGRAM 4.8, PAGE 189
---------------------

.. code:: python

    #Using an array iterator
    def main():
        x = [0,1,2]
        for y in x:
            print y,
    if __name__ == "__main__":
        main()

.. parsed-literal::

    0 1 2


PROGRAM 4.9, PAGE 190
---------------------

.. code:: python

    #Code to simulate C++:STL copy function
    
    def copy(src, target, start, end, to):
        '''Copy form src[start:end] to target[to:(to+end-start)]'''
        while start <= end:
            target.__setitem__(to,src[start])
            #Set item is used for inplace assignment
            to += 1
            start += 1
            
    #Sample I/O - Not in textbook
    a = [1,2,3,4,5,6]
    b = [6,4,0,1,2,3]
    copy(a,b,2,5,2)
    #copies a[2:5] to b[2:5]
    print b

.. parsed-literal::

    [6, 4, 3, 4, 5, 6]


PROGRAM 4.10, PAGE 191
----------------------

.. code:: python

    #Forward chain iterator for Chain class
    class ChainIterator:
        def __init__(self, startNode = None):
            self.current = startNode
        #Python does not support ++ operator hence add method is overloaded.
        def __add__(self,value):
            if value is int:
                for i in range(value):
                    if self.current == None:
                        break
                    self.current = self.current.link
                    return self
            else:
                raise TypeError
        def __ne__(self, right):
            return self.current != right.current
        def __eq__(self, right):
            return self.current == right.current
        
        # This is vaguely equivalent to overloading the . operator
        # This basically allows accessing the members / attributes of the self.current from the interator instance itself.
        __getattr__ = lambda self : self.current.__getattribute__(key)
        
        def __getattr__(self, key):
            return self.current.__getattr__(key)
    
    # Defining ChainIterator as a member object of Chain class
    Chain.ChainIterator = ChainIterator
    
    # Refer Page No 190
    
    # Defining begin and end methods of Chain
        
    Chain.begin = lambda self : self.ChainIterator(self.first)
    Chain.end   = lambda self : self.ChainIterator(None)
PROGRAM 4.11, PAGE 192
----------------------

.. code:: python

    #Inserting at the back of a list
    
    def InsertBack(self, e):
        if self.first == None :
            #If chain is empty
            self.first = ChainNode(e)
            self.last = self.first
        else:
            #On non empty chains
            self.last.link = ChainNode(e)
            self.last = self.last.link
            
    Chain.InsertBack = InsertBack
PROGRAM 4.12, PAGE 192
----------------------

.. code:: python

    #Concatenating two chains
    def Concatenate(b):
        '''b is concatenated to the end of self'''
        if first != None :
            self.last.link = b.first
            self.last = b.last
        else:
            self.first = b.first
            self.last = b.last
        b.first = None
        b.last = None     
    Chain.Concatenate = Concatenate
PROGRAM 4.13, PAGE 193
----------------------

.. code:: python

    #Reversing a list
    def Reverse(self):
        ''' A chain is reversed so that [ a[0] , ... , a[n] ] becomes [ a[n] , ... , a[0] ]'''
        previous = None
        current = self.first
        while current is not None:
            r = previous
            #r is a temp variable which trails the previous
            previous = current
            current = current.link
            previous.link = r
        self.first = previous
    Chain.Reverse = Reverse
PROGRAM 4.14, PAGE 196
----------------------

.. code:: python

    class CircularList:
        def __init__(self):
            self.first = None
            self.last = None
            self.av = None
            #av is the list of deleted Nodes
        def InsertFront(self,e):
            '''Inserts the element e at the front of the circular list self, where last points to the last node in the list'''
            newNode = ChainNode(e)
            if last is not None:
                newNode.link = self.last.link
                self.last.link = newNode
            else:
                #empty list
                self.last = newNode
                self.last.link = self.last
                #circular referencing
PROGRAM 4.15, PAGE 198
----------------------

.. code:: python

    #Getting a Node
    def GetNode(self):
        '''Provide a node for use'''
        if self.av is not None:
            x = self.av
            self.av = self.av.link
        else:
            #if there is no deleted node to x is assigned a new Node
            x = ChainNode()
        return x
    CircularList.GetNode = GetNode
PROGRAM 4.16, PAGE 198
----------------------

.. code:: python

    #Returning a node
    def RetNode(self,x):
        '''Free the node pointed by x'''
        x.link = self.av
        self.av = x
        x = None
        #inserts (at the front) the x to the list av, which contains deleted list
PROGRAM 4.17, PAGE 198
----------------------

.. code:: python

    #Deleting a Circular list
    #Python manages out of scope variable by efficient garbage collection methods hence destructors need not be defined in python
    #Instead a method __del__() is created to simulate the same effect.
    def __del__(self):
        '''Delete the circular list'''
        if self.last is not None:
            self.first = self.last.link
            self.last.link = self.av
            self.av = self.first
            self.last = None
    CircularList.__del__ = __del__
PROGRAM 4.19, PAGE 200
----------------------

.. code:: python

    #Adding a linked stack
    class LinkedStack:
        def __init__(self):
            self.top = None
        def Push(self,e):
            self.top = ChainNode(e,top)
        def IsEmpty(self):
            return self.top is None       
PROGRAM 4.20, PAGE 201
----------------------

.. code:: python

    #Deleting from a Linked Stack
    def Pop(self):
        '''Deleting top node from the stack'''
        if (self.IsEmpty()):
            raise Exception('Stack is empty. Cannot delete')
        delNode = self.top
        sel.top = self.top.link
        #In python the del operator deletes the name from the name space only
        #Automatic garbage collection in python frees the allocated space by itself hence the use of del is not required
    LinkedStack.Pop = Pop
PROGRAM 4.21, PAGE 201
----------------------

.. code:: python

    #Adding to a linked queue
    class LinkedQueue:
        def __init__(self):
            self.front = None
            self.rear = None
        def Push(self,e):
            if(self.IsEmpty()):
                self.rear = self.front = ChainNode(e,None)
            else:
                self.rear.link = ChainNode(e,None)
        def IsEmpty(self):
            if(self.front is None):
                return True
            else:
                return False
PROGRAM 4.22, PAGE 201
----------------------

.. code:: python

    # Deleting from a linked queue
    def _pop(self):
        if(self.IsEmpty()):
            raise Exception("Queue is empty. Cannot delete")
        self.front = self.front.link
    LinkedQueue.pop = _pop
PROGRAM 4.23, PAGE 203
----------------------

.. code:: python

    # Polynomial class definition
    class Term:
        def __init__(self, c = None, e = None):
            self.coef = c
            self.exp = e
            lambda Set : self(c,e)
            self.Set = Set
    
    class Polynomial:
        def __init__(self):
            poly = Chain()   # Instantiating a Chain object with an instance of Term as its attribute first.
PROGRAM 4.24, PAGE 206
----------------------

.. code:: python

    # Adding two polynomials
    def _add(self, b):
        """
        Polynomials self (a) and b are added and the sum is returned
        """
        temp = Term()
        ai = poly.begin()
        bi = b.poly.begin()
        c = Polynomial
        
        while ai is not None and bi is not None:
            if ai.exp == bi.exp:
                sum_ = ai.coef + bi.coef
                if sum_ != 0:
                    c.poly.InsertBack(temp.Set(sum_,ai.exp))
                    ai += 1
                    bi += 1
            elif ai.exp < bi.exp:
                c.poly.InsertBack(temp.Set(bi.coef, bi.exp))
            else:
                c.poly.InsertBack(temp.Set(ai.coef, ai.exp))
                
        while ai != 0:
            # Copy rest of a
            c.poly.InsertBack(temp.Set(ai.coef, ai.exp))
            ai += 1
            
        while bi != 0:
            # Copy rest of b
            c.poly.InsertBack(temp.Set(bi.coef, bi.exp))
            bi += 1
                
        return c
    
    # Overloading the Polynomial's __add__ method ( overloading the + operator for Polynomial class)
    Polynomial.__add__ = _add
PROGRAM 4.26, PAGE 212   &   PROGRAM 4.27, PAGE 213   &   PROGRAM 4.28, PAGE 214
--------------------------------------------------------------------------------

.. code:: python

    # Function to find equivalence classes
    class ENode:
        def __init__(self, d = 0, link = None):
            self.data = d
            self.link = link
    
    def Equivalence():
        """
        Input equivalence pairs and output the equivalence classes.
        """
        inFileContent = None
        try:
            with open("equiv.in", "r") as inFile:
                inFileContent = [ int(i) for i in inFile.read().replace(',',' ').split() ]
                # Stores the file contents as an array of type int.
        except Exception, e:
            print "Cannot open input file"
            return
        
        n = inFileContent[0]
        first = [ ENode(0) for i in range(n) ]
        out = [False]*n
    
        # p is a variable to iterate through the length of the inFileContent
        p = 1
        
        # Phase 1 : Input equivalence pairs
        while p < len(inFileContent):
            i = inFileContent[p]; j = inFileContent[p+1]
            first[i] = ENode(j, first[i])
            first[j] = ENode(i, first[j])
            p += 2
        
        #Phase 2 : Output Equivalence classes
        for i in range(n):
            if not out[i]:
                print "\nA new class", i,
                out[i] = True
                x = first[i]
                top = None
                while True:  # Find the rest of the class
                    while x is not None:  # Process the list
                        j = x.data
                        if not out[j]:
                            print ",", j, 
                            out[j] = True
                            y = x.link
                            x.link = top
                            top = x
                            x = y
                        else:
                            x = x.link
                    # End of while loop
    
                    if not top:
                        break
    
                    x = first[top.data]
                    top = top.link # Unstack
    
                # End of while True
    
            # End of if not out[i]
    
            # In python Garbage Collection is automatic
            
    # Sample Example - Refer Page 211
    with open('equiv.in','w') as f:
        f.write('12 0 4 3 1 6 10 8 9 7 4 6 8 3 5 2 11 11 0')
        
    Equivalence()

.. parsed-literal::

    
    A new class 0 , 11 , 4 , 7 , 2 
    A new class 1 , 3 , 5 
    A new class 6 , 8 , 10 , 9


PROGRAM 4.29, PAGE 219
----------------------

.. code:: python

    # Class Definitions for sparse matrix
    class Triple:
        def __init__(self):
            self.row   = None
            self.col   = None
            self.value = None
    
    class MatrixNode:
        def __init__(self, b, t):
            if ( type(b) != bool ):
                raise TypeError
                return
            
            self.head = b
            
            if b:
                self.right = self.down = self
                self.next_ = None
            else:
                self.triple = t
                
           
    
    class Matrix:
        def __init__(self):
            self.headnode = None
            self.av = None
PROGRAM 4.30, PAGE 221
----------------------

.. code:: python

    # Reading in the Sparse Matrix
    
    #Overloading Operator >> for Class Matrix
    import operator, sys, io, IPython
    
    class MyStdIn(object):
        def __init__(self):
            pass
            
        def __rshift__(self, matrix):
            if isinstance(matrix, Matrix):    
                s = Triple()
                
                # Accept inputs as triplets
                # >>> 5 6 7
                # >>> 1 2 3 etc ...
                
                triplet = raw_input().strip().split()
                    
                s.row, s.col, s.value = [ int(i) for i in triplet ]
                    
                p = max(s.row, s.col)
                
                # Set up header node for list of header Nodes
                matrix.headnode = MatrixNode(False, s)
                
                # If there is no row or column to input
                if p == 0:
                    matrix.headnode.right = matrix.headnode
                    return
                
                # If there is atleast one row or column
                head = [ MatrixNode(True, None) for i in range(p)]
                
                currentRow = 0
                last = head[0]   # Last node in current row
                
                for i in range(s.value):
                    t = Triple()
                    triplet = raw_input().strip().split()
                    
                    t.row, t.col, t.value = [ int(i) for i in triplet ]
                    if  t.row > currentRow:
                        # Close current Row
                        last.right = head[currentRow]
                        currentRow = t.row
                        last = head[currentRow]
                
                    # End of if
                    last = last.right = MatrixNode(False, t)  # Link new node into row list
                    head[t.col].next_ = head[t.col].down = last # Link into column list
                
                # End of for
                last.right = head[currentRow]  # Close last row
                
                for i in range(s.col):
                    head[i].next_.down = head[i] # Close all column lists
                    
                # Link the header nodes together
                for  i in range(p-1):
                    head[i].next_ = head[i+1]
                    
                head[p-1].next = matrix.headnode
                matrix.headnode.right = head[0]
                
                return
            
            else:
                for k, v in list(globals().iteritems()):
                    if (id(v) == id(matrix)) and (k != "matrix"):
                        globals()[k] = raw_input()
                        return
                
    #A new MyStdIn Class inheriting the elements of stdin <file class> [InStream Object Class] is created with the 
    #overloaded operator function __rshift__. 
    
    #Operator >> is specified as a function __rshift__() [Equivalent to c++ style 'operator>>']
.. code:: python

    # So to emulate a C++ style cin we can have :
    
    print "Standard input"
    cin = MyStdIn()
    a = 'Text Before' # Otherwise NameError is raised; This is similar to declarations in C++
    cin>>a
    print type(a), a

.. parsed-literal::

    Standard input
    New Text
    <type 'str'> New Text


.. code:: python

    print "\nMatrix Input"
    # For a Matrix we have:
    m = Matrix()
    # Matrix input is Given as :
    # NUM_ROW NUM_COL NUM_NON_ZERO_ELEMENTS
    # ROW COL VALUE
    # ROW COL VALUE
    #      .
    #      .
    #      .
    #      .
    
    cin>>m  # Refer Page 220 for Input format
    
    # Matrix Input
    # 2 2 2
    # 1 1 2
    # 1 0 4
    
    print "\nFirst Element of the Matrix: ",
    first_cell = m.headnode.right.down.triple
    print (first_cell.row, first_cell.col, first_cell.value)

.. parsed-literal::

    
    Matrix Input
    2 2 2
    1 1 2
    1 0 4
    
    First Element of the Matrix:  (1, 0, 4)


PROGRAM 4.31, PAGE 222
----------------------

.. code:: python

    def _del(self):
        # Return all nodes to the av list. This list is a chain linked via the right field.
        # av is a static variable that points to the first node of the av list.
        if self.headnode is None:
            return # No nodes to delete
        
        x = headnode.right
        self.headnode.right = self.av
        self.av = self.headnode # Return headnode
        
        while x!=self.headnode:
            # Erase by rows
            y = x.right
            x.right = self.av
            self.av = y
            x = x.next_ # Next row
        
        self.headnode = None
    
    Matrix.__del__ = _del
PROGRAM 4.32, PAGE 226
----------------------

.. code:: python

    # Class definition of a doubly linked list
    
    class DblListNode:
        def __init__(self):
            self.data = None
            self.left = self.right = None
            
    class DblList:
        def __init__(self):
            self.first = DblListNode()
PROGRAM 4.33, PAGE 227
----------------------

.. code:: python

    # Deleting from a doubly linked circular list
    def _delete(self, x):
        if  x == self.first:
            raise(Exception("Deletion of header node is not permitted"))
        else:
            x.left.right = x.right
            x.right.left = x.left
            
    DblList.Delete = _delete
PROGRAM 4.34, PAGE 227
----------------------

.. code:: python

    # Insertion into a doubly linked circular list
    def _insert(self, p, x):
        """ Insert into node p to the right of node x """
        p.left = x; p.right = x.right
        x.right.left = p; x.right = p
PROGRAM 4.35, PAGE 233
----------------------

.. code:: python

    # Copying a list
    # Driver
    
    # Class Definition for GenList - Refer Page 231
    class GenList:
        def __init__(self):
            self.first = GenListNode()
    
    class GenListNode:
        def __init__(self):
            self.tag = False
            self.data = None
            self.down = None
            
            self.ref = 0 # Refer Page 238
            self.next_ = None
    
    def _copy(self, l):
        """Make a copy of l"""
        if isinstance(l, GenList):
            self.first = self.Copy(l.first)
            return None
        else:
            q = None
            if l is not None:
                q = GenListNode()
                q.tag = p.tag
                if p.tag:
                    q.down = Copy(p.down)
                else:
                    q.data = p.data
                    
                q.next_ = self.Copy(p.next_)
            return q
        
    GenList.Copy = _copy
PROGRAM 4.36, PAGE 235
----------------------

.. code:: python

    # Determining if two lists are identical
    
    def _eq(self, l):
        return self.Equal(self, l)
    
    def _equal(self, s, l):
        if ( s is None ) and ( t is None ):
            return True
        if ( s and t and ( s.tag == t.tag )):
            if s.tag:
                return self.Equal(s.down, t.down) and self.Equal(s.next_ and t.next_)
            else:
                return ( s.data == t.data ) and self.Equal(s.next_, t.next_)
        return False
    
    GenList.__eq__ = _eq    # Overloading the equality operator.
    GenList.Equal = _equal
PROGRAM 4.37, PAGE 236
----------------------

.. code:: python

    # Driver
    def _depth(self, s = -1):
        if s == -1:   # Pseudo - Function overloading
            return Depth(first)
        else:
            # Workhorse
            if s is None:
                return None
            
            current = s
            m = 0
            
            while current is not None:
                if current.tag:
                    m = max(m, Depth(current.down))
                    current = current.next_
                    
            return m+1
    GenList.Depth = _depth
PROGRAM 4.38, PAGE 239
----------------------

.. code:: python

    # Deleting a list recursively
    # Driver
    
    def _del(self, *inputs):
        
        if len(inputs == 0):
            if first is None:
                self.Delete(first)
                first = None
                return
        
        x = inputs[0]  # Pseudo Function Overloading
        
        x.ref  -= x.ref
        if x.ref != 0:
            y = x
            while y.next_ is not None:
                y = y.next_
                if y.tag == 1:
                    self.Delete(y.down)
            y.next_ = self.av # Attach top level node to av list
            self.av = x