
CHAPTER 2 - ARRAYS
==================

PROGRAM 2.1, PAGE 75
--------------------

.. code:: python

    #Definition of Class Rectangle
    import numpy
    
    class Rectangle:
        def __init__(self,x=None,y=None,h=None,w=None):
            '''Constructor of Rectangle'''
            pass
        def __del__(self):
            '''Destructor of Rectangle'''
            pass
        def GetHeight(self):
            '''returns Height of rectangle'''
            pass
        def GetWidth(self):
            '''Returns Width of rectangle'''
            pass
        __xLow = None
        __yLow = None
        __height = None
        __width = None
        #In python attributes starting with a double underscore are equivalent to private attributes in C++
PROGRAM 2.2, PAGE 76
--------------------

.. code:: python

    #Implementations of Operations on Rectangle
    def GetHeight(self):
        return self._Rectangle__height
    def GetWidth(self):
        return self._Rectangle__width
    #Private variables in python are defined by __<varname> and called using _<class>__<varname>
    
    Rectangle.GetHeight = GetHeight
    Rectangle.GetWidth = GetWidth
    
    #This is the C++ equivalent to defining class methods outside the class. [ using class::member() {} ]
PROGRAM 2.4, PAGE 78
--------------------

.. code:: python

    #Definition Of Constructor For Rectangle
    
    #NOTE: PROGRAM 2.4 [WHICH CONTAINS THE CONSTRUCTOR CLASS DEFINITION, DEFINED OUTSIDE THE CLASS]
    #MUST BE EXECUTED BEFORE PROGRAM 2.3 TO GET CORRECT RESULTS. SO THE ORDER HAS BEEN CHANGED TO FACILITATE THIS
    
    def initfn(self,x=None,y=None,h=None,w=None):
        '''Constructor for class Rectangle'''
        self._Rectangle__xLow = x
        self._Rectangle__yLow = x
        self._Rectangle__height = h
        self._Rectangle__width = w
    Rectangle.__init__ = initfn
PROGRAM 2.3, PAGE 77
--------------------

.. code:: python

    #A Code Fragment demonstrating how Rectangle objects are declared and member functions invoked
    r = Rectangle(1,2,5,6)
    s = Rectangle(1,2,8,9)
    # Values passed to initiate are not a part of the textbook example. This is required to avoid TypeError
    # The Type error when defined as r = Rectangle() [as given in textbook] will be as follows:
    # TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
    
    t = s
    #NOTE: Python has no pointer implementation.
    
    if ( r.GetHeight() * r.GetWidth() ) > ( t.GetHeight() * t.GetWidth() ):
        print 'r',
    else:
        print 's',
    print 'has the greater area'

.. parsed-literal::

    s has the greater area


PROGRAM 2.5, PAGE 78
--------------------

.. code:: python

    #Member Initialization List is not possible in Python
PROGRAM 2.6, PAGE 80
--------------------

.. code:: python

    #Program 2.5 Skipped since Initialization through Member Initialization List [as in C++] 
    #is not possible in Python
    
    #PROGRAM 2.6
    #Overloading Operator == For Class Rectangle
    
    #Operator == is specified as a function __eq__(op1,op2)
    
    def __eq__(self,rhs):
        if (self._Rectangle__xLow == rhs._Rectangle__xLow) and (self._Rectangle__yLow == rhs._Rectangle__yLow) :
            return True
        else:
            return False
    Rectangle.__eq__ = __eq__
    
    #SAMPLE O/P - NOT A PART OF TEXTBOOK:
    print r == s

.. parsed-literal::

    True


PROGRAM 2.7, PAGE 80
--------------------

.. code:: python

    #Overloading Operator << for Class Rectangle
    import operator, sys, io, IPython
    class MyStdout(IPython.kernel.zmq.iostream.OutStream):
        def __init__(self):
            self.__dict__ = sys.stdout.__dict__.copy()
    #All elements of sys.stdout are copied to the MyStdout [inherited class]
    
        def __lshift__(self,rect_instance):
            if isinstance(rect_instance, Rectangle):    
                self.write('Position is:'+str(rect_instance._Rectangle__xLow)+' '+str(rect_instance._Rectangle__yLow))
                self.write('\nHeight is: '+str(rect_instance._Rectangle__height))
                self.write('\nWidth is: '+str(rect_instance._Rectangle__width))
            else:
                self.write(rect_instance)
                
    #A new MyStdout Class inheriting the elements of stdout <file class> [OutStream Object Class] is created with the 
    #overloaded operator function __lshift__. 
    
    sys.stdout = MyStdout()
    
    #an instance of MyStdout is then assigned to sys.stdout
    
    #Operator << is specified as a function __lshift__() [Equivalent to c++ style 'operator<<'
.. code:: python

    #Sample I/O - Not in Text Book
    # C++ Style I/O using << operator overloading in python !
    cout = sys.stdout
    endl = '\n'
    
    cout<<r
    
    #r is an instance of the Rectangle Class Defined earlier
    
    cout<<endl
    cout<<'Sample Text to emphasize the fact that base functionality of sys.stdout remains unchanged'

.. parsed-literal::

    Position is:1 1
    Height is: 5
    Width is: 6
    Sample Text to emphasize the fact that base functionality of sys.stdout remains unchanged

ADT 2.1, PAGE NO 82
-------------------

.. code:: python

    #Abstract Data Type NaturalNumber : 
    class NaturalNumber():
        def __init__(self,value = 0):
            self.value = 0
        def IsZero(self):
            if self.__value__ == 0 : 
                return True
            return False
        def __add__(self,y):
            '''overloading + operator'''
            if isinstance(y, NaturalNumber):
                return self.value + y.value
            elif type(y) in [int, float, long]:
                return self.value + int(y)
            else:
                raise(TypeError)
        def __eq__(self,y):
            '''overloading == operator'''
            if isinstance(y, NaturalNumber):
                return self.value == y.value
            elif type(y) in [int,float,long]:
                return self.value == y
            else:
                raise(TypeError)
        def Successor(self):
            return self.value+1
    #Python has no limit on number size [virtually]. The max no can be understood as "inf".
        def __sub__(self,y):
            '''overloading + operator'''
            if isinstance(y, NaturalNumber):
                res = self.value - y.value
            elif type(y) in [int,float,long]:
                res = self.value + y
            else:
                raise(TypeError)
            return res if res >= 0 else 0

ADT 2.2, PAGE 85
----------------

.. code:: python

    #Abstract Data Type GeneralArray
    defaultValue = 0
    class GeneralArray:
        def __init__(self,j,List,initValue = defaultValue):
            pass
        def Retrieve(self,index):
            pass
        def Store(self,index,x):
            x = float(x)
            pass   
ADT 2.3, PAGE 88   &   PROGRAM 2.8, PAGE 91   &   PROGRAM 2.9, PAGE 92
----------------------------------------------------------------------

.. code:: python

    #Adding two Polynomials
    
    #Declaring and Defining Prerequisites Term and Polynomial
    
    #Class Terms to define a single term of a polynomial.
    
    #Refer Page 90
    class Term:
        def __init__(self):
            self.coef = 0.0
            self.exp = 0
    
    #Abstract data type Polynomial - Representation 3 [ Refer Page 89 ]
    
    class Polynomial:
        def __init__(self,d=0):
            self.degree = d
            self.coeff = [0.0]
            self.termArray = []
            self.terms = 0
            pass
    
    #Method NewTerm to add a new term to the polynomial [ Refer Program 2.9, Page 92 ]
    
        def NewTerm(self,theCoeff,theExp):
            NewTrm = Term()
            NewTrm.coef = theCoeff
            NewTrm.exp = theExp
            self.termArray.append(NewTrm)
            self.terms += 1
            self.degree = max(self.degree, theExp)        
            
    #Method Add to add two polynomials
    
        def Add(self,Polynomial_b):
            if isinstance(Polynomial_b, Polynomial):
                c = Polynomial()
                aPos = 0
                bPos = 0
                while ( aPos<self.terms ) and ( bPos<Polynomial_b.terms ) :
                    #Similar Power terms
                    if termArray[aPos].exp == Polynomial_b.termArray[bPos].exp :
                        t = float(termArray[aPos].coef) + float(Polynomial_b.termArray[bPos].coef)
                        if t != 0 :
                            c.NewTerm(t, self.termArray[aPos].exp)
                            aPos += 1
                            bPos += 1
                    #Dissimilar Power terms
                    elif termArray[aPos].exp < b.termArray[bPos].exp:
                        c.NewTerm(Polynomial_b.termArray[bPos].coef,Polynomial_b.termArray[bPos].exp)
                        bPos += 1
                    else:
                        c.NewTerm(self.termArray[aPos].coef,self.termArray[aPos].exp)
                        aPos += 1
                #Leftover terms of a
                while aPos < self.terms:
                    c.NewTerm(self.termArray[aPos].coef,self.termArray[aPos].exp)
                    aPos += 1
                #Leftover terms of b
                while bPos < Polynomial_b.terms:
                    c.NewTerm(Polynomial_b.termArray[bPos].coef,Polynomial_b.termArray[bPos].exp)
                    bPos += 1
                #C contains the resulting polynomial
                return c
            else:
                raise(TypeError)
    
    #     #Overloading Operator + to do the same funcition as Polynomial_a.Add(Polynomial_b)
    #     #NOTE - This is not a part of the Textbook code - This is added just to enhance usability
    
        def __add__(self,Polynomial_b):
            return Polynomial.Add(self,Polynomial_b) 
ADT 2.4, PAGE 97
----------------

.. code:: python

    #Abstract Data Type SparseMatrix
    
    class MatrixTerm(object):
        def __init__(self,row=None,col=None,value=None):
            self.row = row
            self.col = col
            self.value = value
    
    class SparseMatrix(object):
        '''A Set of triples <row, column, value>, where row and column are non-negative integers
           and form a unique combination; value is also an integer '''
        def __init__(self, r, c, t):
            '''The constructor function creates a SparseMatrix with
               r rows c columns and a capacity of t nonzero terms.'''
            self._SparseMatrix__rows = r
            self._SparseMatrix__cols = c
            self._SparseMatrix__terms = t
            self._SparseMatrix__capacity = t
            self._SparseMatrix__smArray = []
            for i in  range(t):
                self._SparseMatrix__smArray.append(MatrixTerm())
            #The self._SparseMatrix__<var_name> is used to call private members which have been declared by __<var_name>
        def Transpose(self):
            '''Returns the SparseMatrix obtained by interchanging the row 
               and the column value of every triple in self'''
            #self is comparable with *this in c++
            pass
        def Add(self, b):
            '''If the dimensions of self and b are the same, them the matrix produced by 
               adding corresponding items, namely those with identical row and column
               values is returned; otherwise, an exception is thrown.'''
            pass
        def Multiply(self, b):
            '''If the number of columns in self equals the number of rows in b then
               the matrix d produced by multiplying self and b according to the formula
               d[i][j] = summation of ( a[i][k].b[k][j] ), where d[i][j] is the (i,j)th element,
               is returned.
               k ranges from 0 to one less than the number of columns in self
               otherwise an exception is thrown'''
            pass
PROGRAM 2.10, PAGE 100
----------------------

.. code:: python

    #Transposing a Matrix
    def Transpose(self):
        '''Returns the transpose of self'''
        b = SparseMatrix(self._SparseMatrix__rows,self._SparseMatrix__cols,self._SparseMatrix__terms)
        if(self._SparseMatrix__terms>0):
            #Non Zero matrix
            currentB = 0
            for c in range(self._SparseMatrix__cols):
                for i in range(self._SparseMatrix__terms):
                    #Find and move terms in column c
                    if self._SparseMatrix__smArray[i].col == c:
                        term = MatrixTerm(c,self._SparseMatrix__smArray[i].row,self._SparseMatrix__smArray[i].value)
                        b._SparseMatrix__smArray[currentB] = term
                        currentB += 1
            return b
    SparseMatrix.Transpose = Transpose
PROGRAM 2.11, PAGE 102
----------------------

.. code:: python

    #Transposing a Matrix faster
    
    def FastTranspose(self):
        #Return the transpose of self in O(terms + cols) time.
        #The rows and column numbers in each term will be swapped.
        #This transposes self and copies the transposed matrix to b in O(terms + cols)
        b = SparseMatrix(self._SparseMatrix__cols,self._SparseMatrix__rows,self._SparseMatrix__terms)
        if self._SparseMatrix__terms>0:
            cols = self._SparseMatrix__cols
            terms = self._SparseMatrix__terms
            smArray = self._SparseMatrix__smArray
            rowSize = [0]*cols
            rowStart = [0]*cols
            for i in range(terms):    rowSize[smArray[i].col] += 1
            rowStart[0] = 0
            for i in range(1,cols):    rowStart[i] = rowStart[i-1] + rowSize[i-1]
            for i in range(terms):
                j = rowStart[smArray[i].col]
                b._SparseMatrix__smArray[j].row = smArray[i].col
                b._SparseMatrix__smArray[j].col = smArray[i].row
                b._SparseMatrix__smArray[j].value = smArray[i].value
                rowStart[smArray[i].col] += 1
        return b
    SparseMatrix.FastTranspose = FastTranspose
.. code:: python

    #Sample I/O - Not in Textbook
    
    def getMatrix(self,array):
        try:
            for i in range(len(array)):
                tupl = array[i]
                a._SparseMatrix__smArray[i] = MatrixTerm(tupl[0],tupl[1],tupl[2])
        except Exception,e:
            pass
            
    def printMatrix(self):
        bmat = numpy.zeros((self._SparseMatrix__rows,self._SparseMatrix__cols))
        for term in self._SparseMatrix__smArray:
            try:
                bmat[term.row][term.col] = term.value
            except Exception, e:
                pass
        print bmat
    
    a = SparseMatrix(7,7,5)
    getMatrix(a,[(1,2,8),(1,6,6),(3,2,3),(3,4,4),(5,4,5)])
    print  'Matrix a\n'
    printMatrix(a)
    #tra = a.Transpose()
    tra = a.FastTranspose()
    print '\nTranspose of a\n'
    printMatrix(tra)

.. parsed-literal::

    Matrix a
    
    [[ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  8.  0.  0.  0.  6.]
     [ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  3.  0.  4.  0.  0.]
     [ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  0.  0.  5.  0.  0.]
     [ 0.  0.  0.  0.  0.  0.  0.]]
    
    Transpose of a
    
    [[ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  8.  0.  3.  0.  0.  0.]
     [ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  0.  4.  0.  5.  0.]
     [ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  6.  0.  0.  0.  0.  0.]]


PROGRAM 2.12, PAGE 103
----------------------

.. code:: python

    #Storing a Matrix Term
    
    def StoreSum(self,Sum,r,c):
        #If sum != 0, then it is stored along with r and c as last term in self
        if Sum != 0:
            if self._SparseMatrix__terms == self._SparseMatrix__capacity:
                self.ChangeSize1D(2*self._SparseMatrix__capacity)
            self._SparseMatrix__smArray[self._SparseMatrix__terms].row = r
            self._SparseMatrix__smArray[self._SparseMatrix__terms].col = c
            self._SparseMatrix__smArray[self._SparseMatrix__terms].value = Sum
            self._SparseMatrix__terms += 1
    SparseMatrix.StoreSum = StoreSum
PROGRAM 2.13, PAGE 104
----------------------

.. code:: python

    #Change the Size of 1 - Dimensional array
    def ChangeSize1D(self, newSize):
        #Change the size of smArray to newSize
        if newSize < self._SparseMatrix__terms:
            raise Exception('New Size must be >= number of terms')
        for i in range(newSize - self._SparseMatrix__terms):
            self._SparseMatrix__smArray.append(MatrixTerm())
        self._SparseMatrix__capacity = newSize
        if newSize == 0:
            self._SparseMatrix__smArray.append(MatrixTerm())
            self._SparseMatrix__capacity = 1
    SparseMatrix.ChangeSize1D = ChangeSize1D
PROGRAM 2.14, PAGE 104 - 106
----------------------------

.. code:: python

    #Multiply Sparse Matrices
    
    def Multiply(self,b):
        '''Return the product of sparse matrices self and b'''
        
        if self._SparseMatrix__cols != b._SparseMatrix__rows:
            raise Exception('Incompatible Matrices')
        bXpose = b.FastTranspose()
        d = SparseMatrix(self._SparseMatrix__rows,b._SparseMatrix__cols,0)
        currRowIndex = 0
        currRowBegin = 0
        currRowA = self._SparseMatrix__smArray[0].row
        #Set boundary conditions
        if self._SparseMatrix__terms == self._SparseMatrix__capacity:
            self.ChangeSize1D(self._SparseMatrix__terms + 1)
        bXpose.ChangeSize1D(bXpose._SparseMatrix__terms + 1)
        self._SparseMatrix__smArray[self._SparseMatrix__terms].row = self._SparseMatrix__rows
        bXpose._SparseMatrix__smArray[b._SparseMatrix__terms].row = b._SparseMatrix__cols
        bXpose._SparseMatrix__smArray[b._SparseMatrix__terms].col = -1
        Sum = 0
        while currRowIndex < self._SparseMatrix__terms :
            #Generate row currentRowA of d
            currColB = bXpose._SparseMatrix__smArray[0].row
            currColIndex = 0
            while currColIndex <= b._SparseMatrix__terms:
                #Multiply row currRowA of self by column currColB of b
                if self._SparseMatrix__smArray[currRowIndex].row != currRowA:
                    #end of row currRowA
                    d.StoreSum(Sum,currRowA,currColB)
                    Sum = 0
                    #resets sum to 0
                    currRowIndex = currRowBegin
                    #Advance to next column
                    while bXpose._SparseMatrix__smArray[currColIndex].row == currColB:
                        currColIndex += 1
                    currColB = bXpose._SparseMatrix__smArray[currColIndex].row
                elif bXpose._SparseMatrix__smArray[currColIndex].row != currColB :
                    #End of column currColB of b
                    d.StoreSum(Sum,currRowA,currColB)
                    Sum = 0
                    #reset sum
                    #set to multiply row currRowA with next column
                    currRowIndex = currRowBegin
                    currColB = bXpose._SparseMatrix__smArray[currColIndex].row
                elif self._SparseMatrix__smArray[currRowIndex].col < bXpose._SparseMatrix__smArray[currColIndex].col :
                    currRowIndex += 1
                elif self._SparseMatrix__smArray[currRowIndex].col == bXpose._SparseMatrix__smArray[currColIndex].col :
                    #Add to sum
                    Sum += self._SparseMatrix__smArray[currColIndex].value * bXpose._SparseMatrix__smArray[currColIndex].value
                    currRowIndex += 1
                    currColIndex += 1
                else: currColIndex += 1
                #Next term in currColB
            while self._SparseMatrix__smArray[currRowIndex].row == currRowA :
                #Advance to next row
                currRowIndex += 1
            currRowBegin = currRowIndex
            currRowA = self._SparseMatrix__smArray[currRowIndex].row
        #To remove the last terms in a and d since the terms are empty:
        d._SparseMatrix__smArray = d._SparseMatrix__smArray[:-1]
        self._SparseMatrix__smArray = self._SparseMatrix__smArray[:-1]
        return d
    SparseMatrix.Multiply = Multiply
.. code:: python

    #Sample I/O, Not in textbook
    mult = a.Multiply(tra)
    print 'Matrix a is \n'
    printMatrix(a)
    print '\nMatrix a into a transpose is :\n'
    printMatrix(mult)

.. parsed-literal::

    Matrix a is 
    
    [[ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  8.  0.  0.  0.  6.]
     [ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  3.  0.  4.  0.  0.]
     [ 0.  0.  0.  0.  0.  0.  0.]
     [ 0.  0.  0.  0.  5.  0.  0.]
     [ 0.  0.  0.  0.  0.  0.  0.]]
    
    Matrix a into a transpose is :
    
    [[   0.    0.    0.    0.    0.    0.    0.]
     [   0.  100.    0.    9.    0.    0.    0.]
     [   0.    0.    0.    0.    0.    0.    0.]
     [   0.   64.    0.   25.    0.   25.    0.]
     [   0.    0.    0.    0.    0.    0.    0.]
     [   0.    0.    0.   16.    0.   25.    0.]
     [   0.    0.    0.    0.    0.    0.    0.]]


ADT 2.5, PAGE 114
-----------------

.. code:: python

    #Abstract Datatype String
    class String(object):
        def __init__(self,init):
            #Constructor that initializes self to string init of length of m
            self._String__Str = init
            self._String__leng = len(init)
            self.FailureFunction()
        def __eq__(self,t):
            #overloading == operators
            if self._String__Str == t._String__t:
                print True
            else:
                print False
        def __not__(self):
            if self._String__Length <= 0:
                print True
            else:
                print False
        def Length(self):
            return self._String__leng
        def Concat(self,t):
            return self._String__Str + t
        def Substr(self,i,j):
            try:
                substr = self._Strint__Str[i:i+j]
                return substr
            except IndexError:
                print 'Invalid values for Substring'
                return None
        def Find(pat):
            '''Returns an index i such that pat matches the substring of self that begins at position of i
               Returns -1 if pat is either empty or not a substring'''
            pass    
PROGRAM 2.15, PAGE 115
----------------------

.. code:: python

    #Exhaustive Pattern Matching
    def Find(self,pat):
        '''Return -1 if pat does not occur in self
           otherwise return the first position in self, where pat begins'''
        for start in range(self.Length()-pat.Length()+1) :
            #Check for match beginning at str[start]
            for j in range(pat.Length()) :
                if self._String__Str[start + j] != pat._String__Str[j]:
                    break
                if j == pat.Length()-1:
                    #Match found
                    return start
        #Pat is empty or does not occur in string:
        return -1  
    
    #NOTE : The entire program can be implemented using python string function as follows: 
    #def FindPythonImplementation(self,pat):
    #    return self._String__Str.find(pat)
    
    String.Find = Find
    #String.Find = FindPythonImplementation
PROGRAM 2.16, PAGE 117
----------------------

.. code:: python

    #Pattern Matching with a Failure Function
    def FastFind(self, pat):
        '''Determine if pat is a substring in O( LengthP + LengthS )'''
        posP = 0
        posS = 0
        lengthP = pat.Length()
        lengthS = self.Length()
        while ( posP < lengthP ) and ( posS < lengthS ):
            if pat._String__Str[posP] == self._String__Str[posS] :
                posP += 1
                posS += 1
            elif posP == 0:
                posS += 1
            else:
                posP = pat.f[posP - 1] + 1
        if posP < lengthP :
            return -1
        else:
            return posS-lengthP
    String.FastFind = FastFind
PROGRAM 2.17, PAGE 118
----------------------

.. code:: python

    #Computing the failure function
    def FailureFunction(self):
        lengthP = self.Length()
        self.f = [0]*lengthP
        self.f[0] = -1
        for j in range(1,lengthP):
            i = self.f[j-1]
            while ( self._String__Str[j] != self._String__Str[i+1] ) and  ( i >= 0 ):
                i = self.f[i]
            if self._String__Str[j] == self._String__Str[i+1]:
                self.f[j] = i + 1
            else:
                self.f[j-1] = -1
    String.FailureFunction = FailureFunction
.. code:: python

    #Sample I/O - Not in textbook
    str1 = String('hello world')
    str2 = String('llo')
    print str1.Find(str2), str1.FastFind(str2)

.. parsed-literal::

    2 2

