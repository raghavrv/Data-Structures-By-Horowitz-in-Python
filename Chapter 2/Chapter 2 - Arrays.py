
# coding: utf-8

# In[1]:

# Imports
import numpy
# For random string generation
from string import ascii_letters
from random import choice
from time import time # For analysis of the running time
import matplotlib.pyplot as plt # to plot the run time analysis


## CHAPTER 2 - ARRAYS

### PROGRAM 2.1, PAGE 75

# In[2]:

# Definition of Class Rectangle

class Rectangle:
    def __init__(self,x=None,y=None,h=None,w=None):
        '''Constructor of Rectangle'''
        pass
    def __del__(self):
        '''Destructor of Rectangle'''
        pass
    def get_height(self):
        '''returns Height of rectangle'''
        pass
    def get_width(self):
        '''Returns Width of rectangle'''
        pass
    _x_low = None
    _y_low = None
    _height = None
    _width = None
    # In python attributes starting with an underscore are conventionaly understood to be private attributes.


### PROGRAM 2.2, PAGE 76

# In[3]:

# Implementations of Operations on Rectangle
def get_height(self):
    return self._height
def get_width(self):
    return self._width

Rectangle.get_height = get_height
Rectangle.get_width = get_width

# This is the closest C++ equivalent to defining class methods outside the class. [ using class::member() {} ]

# Though THIS IS NOT AN ACCEPTED PRACTICE IN PYTHON. This would be an workaround to define 
# the member functions outside of the class definition as and when the functionality of the method in defined
# in the text


### PROGRAM 2.4, PAGE 78

# In[4]:

# Definition Of Constructor For Rectangle

def constructor_for_Rectangle_class(self,x=None,y=None,h=None,w=None):
    '''Constructor for class Rectangle'''
    self._x_low = x
    self._y_low = x
    self._height = h
    self._width = w

# __init__ method is invoked in python when a member of the class is instantiated
Rectangle.__init__ = constructor_for_Rectangle_class


### PROGRAM 2.3, PAGE 77

# In[5]:

r = Rectangle(1,2,5,6)
s = Rectangle(1,2,8,9)

t = s

if ( r.get_height() * r.get_width() ) > ( t.get_height() * t.get_width() ):
    print 'r',
else:
    print 's',

print 'has the greater area'


### PROGRAM 2.6, PAGE 80

# In[6]:

s._x_low


# In[7]:

# Overloading the equality check operator

# Operator == is specified as a function __eq__(op1,op2)

def __eq__(self,rhs):
    if (self._x_low == rhs._x_low) and (self._y_low == rhs._y_low) and ( self._height == rhs._height ) and ( self._width == rhs._width ) :
        return True
    else:
        return False
    
# Overriding the default behaviour of == by defining a __eq__ memeber function
Rectangle.__eq__ = __eq__

# SAMPLE O/P
print r == s


### PROGRAM 2.7, PAGE 80

# In[8]:

# Overloading the right shift operator <<
import operator, sys, io, IPython


class MyStdout(IPython.kernel.zmq.iostream.OutStream):
    """
    MyStdout class inherits from the OutStream of IPython kernel.
    This is done to simulate the C++ OutStream "cout"
    """    
    def __init__(self):
        self.__dict__ = sys.stdout.__dict__.copy()
        # All elements of sys.stdout are copied to the MyStdout [inherited class]

    def __lshift__(self,rect_instance):
        # lshift ( << ) operator is overloaded to allow printing of Rectangle
        
        if isinstance(rect_instance, Rectangle):    
            self.write('Position is:'+str(rect_instance._x_low)+' '+str(rect_instance._y_low))
            self.write('\nHeight is: '+str(rect_instance._height))
            self.write('\nWidth is: '+str(rect_instance._width))
        else:
            self.write(rect_instance)
            
# A new MyStdout Class inheriting the elements of stdout <file class> [OutStream Object Class] is created with the 
# overloaded operator function __lshift__. 

sys.stdout = MyStdout()

#an instance of MyStdout is then assigned to sys.stdout

#Operator << is specified as a function __lshift__() [Equivalent to c++ style 'operator<<'


# In[9]:

# C++ Style I/O using << operator overloading in python !

cout = sys.stdout
endl = '\n'

cout<<r

#r is an instance of the Rectangle Class Defined earlier

cout<<endl
cout<<'Sample Text to emphasize the fact that base functionality of sys.stdout remains unchanged'


### ADT 2.1, PAGE NO 82

# In[10]:

# Abstract Data Type NaturalNumber : 
class NaturalNumber():
    def __init__(self,value = 0):
        self.value = 0
        
    def is_zero(self):
        if self.value == 0 : 
            return True
        return False
    
    def __add__(self,y):
        # overloading + operator
        if isinstance(y, NaturalNumber):
            return self.value + y.value
        elif type(y) in [int, float, long]:
            return self.value + int(y)
        else:
            raise(TypeError)
            
    def __eq__(self,y):
        # overloading == operator
        if isinstance(y, NaturalNumber):
            return self.value == y.value
        elif type(y) in [int,float,long]:
            return self.value == y
        else:
            raise(TypeError)
            
    def successor(self):
        return self.value+1
    
    # Python has no limit on number size [virtually]. The max no can be understood as float("inf")
    
    def __sub__(self,y):
        '''overloading + operator'''
        if isinstance(y, NaturalNumber):
            res = self.value - y.value
        elif type(y) in [int,float,long]:
            res = self.value + y
        else:
            raise(TypeError)
        return res if res >= 0 else 0


### ADT 2.2, PAGE 85

# In[11]:

# Abstract Data Type GeneralArray
default_value = 0

class GeneralArray:
    def __init__(self, j, List, init_value = default_value):
        pass
    def retrieve(self,index):
        pass
    def store(self,index,x):
        x = float(x)
        pass   


### ADT 2.3, PAGE 88 &nbsp; & &nbsp; PROGRAM 2.8, PAGE 91 &nbsp; & &nbsp; PROGRAM 2.9, PAGE 92

# In[12]:

# Adding two Polynomials

# Declaring and Defining Prerequisites Term and Polynomial

# Class Terms to define a single term of a polynomial.

# Refer Page 90

# NOTE : This is just to illustrate how a Polynomial data type can be constructed in Python
# For all practical purposes, use sympy, an efficient symbolic math and Computer Algebra System library in Python

class Term:
    def __init__(self):
        self.coef = 0.0
        self.exp = 0

        
# Abstract data type Polynomial - Representation 3 [ Refer Page 89 ]
class Polynomial:
    def __init__(self,d=0):
        self.degree = d
        self.coeff = [0.0]
        self.term_array = []
        self.terms = 0
        pass

    # Method new_term to add a new term to the polynomial [ Refer Page 92 ]

    def new_term(self,coef,exp):
        NewTrm = Term()
        NewTrm.coef = coef
        NewTrm.exp = exp
        pos = 0
        # Compute the position of the new term ( sorted by exponents )
        while ( pos < self.terms ) and ( self.term_array[pos].exp < NewTrm.exp ):
            pos += 1
            
        # If there is already a term with the given exponent, add the coefficient
        if ( pos < self.terms ) and ( self.term_array[pos].exp == NewTrm.exp ):
            self.term_array[pos].coef += coef
            return
                
        self.term_array.insert(pos, NewTrm)
        self.terms += 1
        self.degree = max(self.degree, exp)        
        
    # Method Add to add two polynomials

    def add(self,Polynomial_b):
        if isinstance(Polynomial_b, Polynomial):
            c = Polynomial()
            a_pos = 0
            b_pos = 0
            while ( a_pos < self.terms ) and ( b_pos < Polynomial_b.terms ) :
                # Similar Power terms
                if self.term_array[a_pos].exp == Polynomial_b.term_array[b_pos].exp :
                    t = float(term_array[a_pos].coef) + float(Polynomial_b.term_array[b_pos].coef)
                    if t != 0 :
                        c.new_term(t, self.term_array[a_pos].exp)
                        a_pos += 1
                        b_pos += 1
                        
                # Dissimilar Power terms
                elif self.term_array[a_pos].exp < Polynomial_b.term_array[b_pos].exp:
                    c.new_term(Polynomial_b.term_array[b_pos].coef, Polynomial_b.term_array[b_pos].exp)
                    b_pos += 1
                else:
                    c.new_term(self.term_array[a_pos].coef, self.term_array[a_pos].exp)
                    c.display()
                    a_pos += 1
                    
            # Leftover terms of a
            while a_pos < self.terms:
                c.new_term(self.term_array[a_pos].coef, self.term_array[a_pos].exp)
                a_pos += 1
                
            # Leftover terms of b
            while b_pos < Polynomial_b.terms:
                c.new_term(Polynomial_b.term_array[b_pos].coef, Polynomial_b.term_array[b_pos].exp)
                b_pos += 1
                
            # C contains the resulting polynomial
            return c
        else:
            raise(TypeError)

    # Overloading Operator + to do the same funcition as Polynomial_a.add(Polynomial_b)

    def __add__(self,Polynomial_b):
        return Polynomial.add(self,Polynomial_b)
    
    def display(self):
        """Display the polynomial using the latex display in IPython notebook. 
        Note that this works only inside IPython notebook"""
        
        from IPython.display import display, Math, Latex
        
        latex = "{"
        
        for t in reversed(self.term_array):
            if t.coef >= 0 and latex != "{" :
                latex += " + "
                
            if t.exp == 0:
                latex += " {coef} ".format(coef=t.coef)
            elif t.exp == 1:
                latex += " {coef}x ".format(coef=t.coef)
            else:
                latex += " {coef}x^{exp} ".format(coef=t.coef, exp=t.exp)
            
        latex += "}"
        
        display(Math(latex))


# ### Example Usage
# $f = {2.5x^2 - 3x + 5}$<br>
# $g = {3.2x^3 - 4x}$<br><br>
# $h = f + g$<br><br>
# $h = {3.2x^3 + 2.5x^2 - 7x + 5}$<br>

# In[13]:

# Example Usage :

f = Polynomial()
f.new_term(2.5, 2); f.new_term(-3, 1); f.new_term(5,0)
f .display()


# In[14]:

g = Polynomial()
g.new_term(3.2, 3); g.new_term(-4, 1);
g.display()


# In[15]:

h = f + g
h.display()


### ADT 2.4, PAGE 97  

# In[16]:

# Abstract Data Type SparseMatrix

class MatrixTerm(object):
    def __init__(self,row=None,col=None,value=None):
        self.row = row
        self.col = col
        self.value = value
    def set_value(self, row=None, col=None, value=None):
        if row is not None:
            self.row = row
        if col is not None:
            self.col = col
        if value is not None:
            self.value = value                

class SparseMatrix(object):
    '''A Set of triples <row, column, value>, where row and column are non-negative integers
       and form a unique combination; value is also an integer '''
    def __init__(self, rows, cols, terms):
        '''The constructor function creates a SparseMatrix with
           r rows c columns and a capacity of t nonzero terms.'''
        self._rows = rows # No of rows
        self._cols = cols # No of cols
        self._terms = terms # No of terms
        # self._capacity = t # This term is not used since in python lists can be extended
        self._sm_array = [ MatrixTerm() for i in range(terms) ] # List which stores the <row, col, value> triplet
        
    def Transpose(self):
        '''Returns the transpose of the SparseMatrix'''
        # self is comparable with *this in c++
        pass
    
    def add(self, b):
        '''Performs matrix addition of self with the b SpareMatrix'''
        pass
    
    def Multiply(self, b):
        '''
        If the number of columns in self equals the number of rows in b, then returns the
        multiplication matrix of self and b.
        If not an exception is thrown
        '''
        pass


### PROGRAM 2.10, PAGE 100

# In[17]:

# Transposing a Matrix
# Runs in O(terms*cols)
# In comparison, the naive method runs in O(rows*cols)

def transpose(self):
    '''Returns the transpose of self'''
    
    tran = SparseMatrix(self._cols, self._rows, self._terms)
    
    if(self._terms < 0):
        # If self is a zero matrix
        return tran
    
    # If self is a Non Zero matrix
    
    tran_term_index = 0
    
    for c in range(self._cols):
        for i in range(self._terms):
            # Find and move terms in column c
            if self._sm_array[i].col == c:
                # Add the i-th term with row number and col number interchanged to the tran matrix
                tran._sm_array[tran_term_index].set_value(row = c, 
                                                          col = self._sm_array[i].row,
                                                          value = self._sm_array[i].value
                                                          )
                tran_term_index += 1
    return tran

SparseMatrix.transpose = transpose


### PROGRAM 2.11, PAGE 102

# In[18]:

# A faster method for transposing of Sparse Matrices
# Runs in O(terms + cols)

def fast_transpose(self):
    
    tran = SparseMatrix(self._cols, self._rows, self._terms)
    
    if self._terms>0:
        cols = self._cols
        terms = self._terms
        sm_array = self._sm_array
        
        # No. of terms in the i-th column => row_size[i] => no of terms in the i-th row of transpose
        row_size = [0]*cols
        
        # Starting index of the sm_array for row i of tran array => row_start[i]
        row_start = [0]*cols
        
        for i in range(terms):
            row_size[sm_array[i].col] += 1
        
        # Based on the no. of terms in the previous row the row start index table can
        # be computed. This helps in speeding up the transpose method.
        for i in range(1,cols):
            row_start[i] = row_start[i-1] + row_size[i-1]
        
        for i in range(terms):
            j = row_start[sm_array[i].col]
            tran._sm_array[j].row = sm_array[i].col
            tran._sm_array[j].col = sm_array[i].row
            tran._sm_array[j].value = sm_array[i].value
            row_start[sm_array[i].col] += 1
            
    return tran

SparseMatrix.fast_transpose = fast_transpose


# In[19]:

def get_matrix(self,array):
    """
    Stores the <row, col, value> triplets in the array to self
    """
    try:
        for i in range(len(array)):
            tupl = array[i]
            a._sm_array[i] = MatrixTerm(tupl[0],tupl[1],tupl[2])
    except Exception,e:
        pass
        
def print_matrix(self):
    bmat = numpy.zeros((self._rows,self._cols))
    for term in self._sm_array:
        try:
            bmat[term.row][term.col] = term.value
        except Exception, e:
            pass
    print bmat

# Helper methods to input an array of <row, col, value> triplets and to print the sparse matrix
SparseMatrix.get_matrix = get_matrix
SparseMatrix.print_matrix = print_matrix

a = SparseMatrix(6,6,8)
get_matrix(a,[(0,0,-15),(0,3,12),(0,5,-5),(1,1,1),(1,2,13),(2,3,-16),(4,0,9),(5,2,12)])
print  'Matrix a\n'
print_matrix(a)


# In[20]:

# Technically timeit should be run on different sized / valued inputs but here the same matrix a
# is transposed repetitively instead to avoid complexity of generating a random sparse matrix

get_ipython().magic(u'timeit a.transpose()')
tra = a.transpose()
print '\nTranspose of a\n'
print_matrix(tra)


# In[21]:

get_ipython().magic(u'timeit a.fast_transpose()')
tra = a.fast_transpose()
print '\nFast Transpose of a\n'
print_matrix(tra)


# In[22]:

# Note that the sm_array has all the triplets ordered by row number.
print "Row\tCol\tValue"
print "======================="
for t in tra._sm_array:
    print "%d\t%d\t%d"%(t.row, t.col, t.value)


### PROGRAM 2.12, PAGE 103

# In[23]:

# Storing a Matrix Term

def add_term(self,val,r,c):
    # If sum != 0, then it is stored along with r and c as last term in self
    if val != 0:
        # Compute the index where the new Term must be inserted into the 
        # sm_array which is ordered by row no
        
        i = 0
        while i < self._terms:
            if self._sm_array[i].row > r:
                break
            i += 1
                
        self._sm_array.insert(i, MatrixTerm(row = r, col = c, value = val))
        self._terms += 1
        
SparseMatrix.add_term = add_term


### PROGRAM 2.14, PAGE 104 - 106

# In[24]:

# Multiply Sparse Matrices
# Works in O(b.cols * a.terms + a.rows * b.terms)
# This outperforms the standard O(a.rows * a.cols * b.cols) time if b.terms and a.terms are relatively low

def multiply(self,b):
    '''Return the product of sparse matrices self and b'''
    
    if self._cols != b._rows:
        raise Exception('Incompatible Matrices.')

    # b transpose makes the sm_array contain terms ordered by columns of b ( rows of bᵀ )
    bXpose = b.fast_transpose()
    
    # The product matrix
    product = SparseMatrix(self._rows, b._cols, 0)
    
    curr_row_index = 0
    curr_row_begin = 0
    curr_row_a = self._sm_array[0].row   # Current row of a that is being multiplied with the col of b
    
    # Introducing terms to help deal with the end condition
    self._sm_array.append(MatrixTerm(row = self._rows, col = -1, value = None))
    bXpose._sm_array.append(MatrixTerm(row = b._cols, col = -1, value = None))
    
    Sum = 0
    
    while curr_row_index < self._terms :
        # Generate row current_row_a of d
        curr_col_b = bXpose._sm_array[0].row
        curr_col_index = 0
        
        while curr_col_index <= b._terms:
            # Multiply row curr_row_a of self by column curr_col_b of b
            
            if self._sm_array[curr_row_index].row != curr_row_a:
                # End of row curr_row_a
                
                # Add the sum to the product matrix at position { curr_row_a, curr_col_b }
                product.add_term(Sum,curr_row_a,curr_col_b)
                
                Sum = 0 # Reset sum to 0
                
                # Reset to the beginning of current row ( of a ) for multiplication with next column ( of b )
                curr_row_index = curr_row_begin
                
                # Advance to next column ( of b )
                while bXpose._sm_array[curr_col_index].row == curr_col_b:
                    curr_col_index += 1
                
                # Note that in Sparse Matrix the terms are arranged in rows
                # bXpose's terms are arranged in columns of b ( or rows of bXpose )
                curr_col_b = bXpose._sm_array[curr_col_index].row
                
            elif bXpose._sm_array[curr_col_index].row != curr_col_b :
                # End of column curr_col_b of b
                
                # Add the sum to the product matrix at position { curr_row_a, curr_col_b }
                product.add_term(Sum,curr_row_a,curr_col_b)
                
                Sum = 0 # Reset sum to 0
                
                # Reset to the beginning of current row ( of a ) for multiplication with next column ( of b )
                curr_row_index = curr_row_begin
                
                # Advance to the next column in b 
                # ( note that bXpose._sm_array[curr_col_index].row points to the next column already )
                curr_col_b = bXpose._sm_array[curr_col_index].row
                
            elif self._sm_array[curr_row_index].col < bXpose._sm_array[curr_col_index].col :
                curr_row_index += 1 # Advance to the next term in row
            
            # FOLLOWING EXPLANATION DIAGRAMS NOT IN TEXTBOOK
            #
            # ( If the following  diagrams appear in two lines shrink your page size to below 100% )
            #
            # In the row curr_row_a, if the current column of the current term is 
            # same as the current row of b ( col of bXpose ) in the curr_col_b column
            # multiply the terms and add to the Sum
            #
            #
            #      a                      b               bXpose            product
            #   
            #   . . 0 .                 . . . 0          . . 0 .            . . . .
            #   0 x . 0 ◀―― curr_row_a  . 0 0 .          . 0 . 0            . . x .  ◀―― Result row
            #   . 0 . .                 0 . . .          . 0 . x ◀─┐        . . . .
            #   0 . 0 .                 . 0 x .          0 . . .   │        . . . . 
            #                               ▲                      │            ▲
            #                               │                curr_col_b         │ 
            #                          curr_col_b                           Result col
            #      
            #    in a       : x = a._sm_matrix[curr_row_index]
            #    in b       : x = b._sm_matrix[curr_col_index]
            #    in product : x is the new term to be added for which the Sum is being computed
            #
            
            elif self._sm_array[curr_row_index].col == bXpose._sm_array[curr_col_index].col :
                # Add to sum
                Sum += self._sm_array[curr_row_index].value * bXpose._sm_array[curr_col_index].value
                curr_row_index += 1
                curr_col_index += 1
                
            else: 
                curr_col_index += 1
                # Next term in curr_col_b
                
        while self._sm_array[curr_row_index].row == curr_row_a :
            # Advance to next row ( of a )
            curr_row_index += 1
            
        curr_row_begin = curr_row_index
        curr_row_a = self._sm_array[curr_row_index].row
        
    # To remove the last terms in a and d since the terms are empty:
    del product._sm_array[-1]
    del self._sm_array[-1]
    del b._sm_array [-1]
    
    return product

SparseMatrix.multiply = multiply


# In[25]:

mult = a.multiply(tra)
print 'Matrix a is \n'
print_matrix(a)
print "\nMatrix a . a' is :\n"
print_matrix(mult)


### ADT 2.5, PAGE 114

# In[26]:

# Abstract Datatype String
class String(object):
    def __init__(self,init):
        # Constructor that initializes self to string init of length of m
        self._str = init
        self._length = len(init)
        self.failure_function()
        
    def __eq__(self,t):
        # overloading == operators
        return self._str == t._str
    
    def __not__(self):
        if self._length <= 0:
            print True
        else:
            print False
            
    def length(self):
        return self._length
    
    def concat(self,left):
        self._str += t
        return self
    
    def substr(self,i,j):
        """
        Return a substring whose starting index is i and length is j
        """
        try:
            substr = self._str[i:i+j]
            return substr
        
        except IndexError:
            print 'Invalid index / length to get Substring'
        
    def find(self, pat):
        '''Returns an index i such that pat matches the substring of self that begins at position of i
           Returns -1 if pat is either empty or not a substring'''
        pass    


### PROGRAM 2.15, PAGE 115

# In[27]:

# Exhaustive Pattern Matching

def find(self,pat):
    '''Return -1 if pat does not occur in self
       otherwise return the first position in self, where pat begins'''
    
    for start in range(self.length()-pat.length()+1) :
        # Check for match beginning at str[start]
        for j in range(pat.length()) :
            # Character by character checking
            
            if self._str[start + j] != pat._str[j]:
                break
                
            if j == pat.length()-1:
                # Match found
                return start
    
    # Pat is empty or does not occur in string
    return -1  

# NOTE : The entire program can be implemented using python string function as follows: 
# self._str.find(pat)

String.find = find


### PROGRAM 2.16, PAGE 117

# In[28]:

# Faster implementation of the find method using the failure array and failure function to 
# allow resuming search at partial matches. The failure vector is stored at String.f

# Runs in O( LengthP + LengthS )

def fast_find(self, pat):
    posP = 0
    posS = 0

    lengthP = pat.length()
    lengthS = self.length()
    
    while ( posP < lengthP ) and ( posS < lengthS ):
        if pat._str[posP] == self._str[posS] :
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
    
String.fast_find = fast_find


### PROGRAM 2.17, PAGE 118

# In[29]:

# Computing the failure function

def failure_function(self):
    lengthP = self.length()
    self.f = [0]*lengthP
    self.f[0] = -1
    for j in range(1,lengthP):
        i = self.f[j-1]
        while ( self._str[j] != self._str[i+1] ) and  ( i >= 0 ):
            i = self.f[i]
        if self._str[j] == self._str[i+1]:
            self.f[j] = i + 1
        else:
            self.f[j-1] = -1
            
String.failure_function = failure_function


# In[30]:

str1 = String('hello world')
str2 = String('sdf')
print str1.find(str2), str1.fast_find(str2)


# In[31]:

str2 = String('ell')
print str1.find(str2), str1.fast_find(str2)


# In[32]:

# Analysing the above two find methods
x_axis = range(10, 1000, 50)
find_run_time = []
fast_find_run_time = []


for i in x_axis:
    string = String(''.join(choice(ascii_letters) for _ in range(i))) # Generates a random string of i chars
    pattern = String(''.join(choice(ascii_letters) for _ in range(i/2))) # Generates a random pattern string of i chars
    start = time()
    for i in range(10):
        string.find(pattern)
    find_run_time.append((time() - start) / 10) # Takes average over 10 runs
    start = time()
    for i in range(10):
        string.fast_find(pattern)
    fast_find_run_time.append((time() - start) / 10)
    

# NOTE: All these are typically failure / worst case run times, 
# since the probability of a random pattern matching with a random string is very low

# Note the quadratic run time of find and linear run time of fast_find
    
get_ipython().magic(u'matplotlib inline')
plt.figure().set_size_inches(10,10)
plt.xlabel("Size of the input string : n ")
plt.ylabel("Time in ms for the find operation")

plt.plot(x_axis, find_run_time, marker = "o", linestyle = "--", c="b", label="find")
plt.plot(x_axis, fast_find_run_time, marker = "o", linestyle = "--", c="r", label="fast_find")
plt.legend()
plt.show()

