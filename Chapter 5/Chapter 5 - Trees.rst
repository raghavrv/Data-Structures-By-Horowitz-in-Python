
Class Definition for Tree and TreeNode - Page 252, Page 257
-----------------------------------------------------------

.. code:: python

    # Binary Tree Class
    
    class TreeNode(object):
        def __init__(self, left = None, data = None, right = None):
            """ Create a new TreeNode """
            self.data = data
            self.rightChild = right
            self.leftChild = left    
    
            
    class Tree(object):
        def __init__(self, root = None ):
            # This implementation differs from the Textbook definition
            # Here Tree is an encapsulation of the root
            # root is a Binary Tree formed by the Linking together TreeNodes
            # This will avoid confusion between Tree and TreeNode
            
            """ Create a new Binary Tree """
            self.root = root
            
        def LeftSubtree(self):
            """ Return Left Sub Tree """
            return self.root.rightChild
        
        def RightSubtree(self):
            """ Return Right Sub Tree """
            return self.root.leftChild
        
        def RootData(self):
            """ Return the root data """
            return self.root.data
        
        def IsEmpty(self):
            """ Returns True if Tree Node is empty """
            return self.root is None
PROGRAM 5.1, PAGE 261
---------------------

.. code:: python

    # Inorder Traversal of a binary Tree
    
    def _inorder(self, currentNode = -1):
        if currentNode != -1:
            if currentNode is not None:
                self.Inorder(currentNode.leftChild)
                self.Visit(currentNode)
                self.Inorder(currentNode.rightChild)
        
        elif self.root is None:
            return None
        
        else:
            self.Inorder(self.root)
            
    def _visit(self, Node):
        print "" if Node is None else Node.data,
    
    Tree.Inorder = _inorder
    Tree.Visit = _visit
PROGRAM 5.2, PAGE 263
---------------------

.. code:: python

    # Preorder traversal of a binary tree
    
    def _preorder(self, currentNode = -1):
        if currentNode != -1:
            if currentNode is not None:
                self.Visit(currentNode)
                self.Preorder(currentNode.leftChild)        
                self.Preorder(currentNode.rightChild)
        
        elif self.root is None:
            return None
        
        else:
            self.Preorder(self.root)
            
    Tree.Preorder = _preorder
PROGRAM 5.3, PAGE 263
---------------------

.. code:: python

    # Postorder traversal of a binary tree
    
    def _postorder(self, currentNode = -1):
        if currentNode != -1:
            if currentNode is not None:
                self.Postorder(currentNode.leftChild)        
                self.Postorder(currentNode.rightChild)
                self.Visit(currentNode)        
    
        elif self.root is None:
            return None
        
        else:
            return self.Postorder(self.root)
    
    Tree.Postorder = _postorder
PROGRAM 5.4, PAGE 264
---------------------

.. code:: python

    # Non recursive inorder traversal
    
    def _nonrecInorder(self):
        """ Non Recursive inorder traversal using a stack """
        s = [] # Using Python List as a stack
        currentNode = self.root
        while True:
            while currentNode is not None:  # move down leftChild field
                s.append(currentNode)  # add to stack
                currentNode = currentNode.leftChild
            if len(s) == 0:
                return
            
            currentNode = s[-1]
            s.pop() # delete from the stack
            self.Visit(currentNode)
            currentNode = currentNode.rightChild
            
    Tree.NonrecInorder = _nonrecInorder
PROGRAM 5.5, PAGE 265
---------------------

.. code:: python

    # Definition of a simple inorder iterator
    
    # In Python it is possible to return an iterable of the object using the iter() method
    # The __iter__() is overloaded to provide custom definition
    
    def _iter(self):
        return self
    
    Tree.__iter__ = _iter
    
    # iter(Tree) will return an iterable whose definition is defined in PROGRAM 5.6  
    # This also works using for
    # for inorder_node in tree1:
    #     <code>
PROGRAM 5.6, PAGE 265
---------------------

.. code:: python

    # Code for obtaining the next inorder element
    def _next(self):
        if "s" not in self.next.__dict__:
            # During every 1st iteration :
            
            self.next.__dict__["s"] = list() # Define an empty list
            # Python equivalent of a C++ static list variable s
        
        if "currentNode" not in self.next.__dict__:
            self.next.__dict__["currentNode"] = self.root
            
        while self.next.currentNode is not None:
            self.next.s.append(self.next.currentNode)
            self.next.__dict__["currentNode"] = self.next.currentNode.leftChild
        
        if len(self.next.s) == 0:
            self.next.__dict__.pop("s")
            self.next.__dict__.pop("currentNode")
            raise StopIteration
        
        self.next.__dict__["currentNode"] = self.next.s.pop()
        
        temp = self.next.currentNode.data
        
        self.next.__dict__["currentNode"] = self.next.currentNode.rightChild
        
        return temp
    
    Tree.next = _next
    
    # A more simpler Python way to iterate over the tree elements in inorder traversal is by using the generator
    # Not given in Text Book
    
    def _InorderIterator(self, tree = -1):
        if tree == -1:
            tree = self.root
        
        if tree is not None:
            for node in self.InorderIterator(tree.leftChild):
                yield node
                
            yield tree.data
            
            for node in self.InorderIterator(tree.rightChild):
                yield node
                
    Tree.InorderIterator = _InorderIterator
PROGRAM 5.7, PAGE 266
---------------------

.. code:: python

    # Level order traversal of Binary tree
    
    def _LevelOrder(self):
        
        q = list() # Using a list as a queue
        currentNode = self.root
        
        while currentNode is not None:
            self.Visit(currentNode)
    
            if currentNode.leftChild:
                q.append(currentNode.leftChild)
            if currentNode.rightChild:
                q.append(currentNode.rightChild)
            if len(q) == 0:
                return
            
            currentNode = q.pop()
            
    Tree.LevelOrder = _LevelOrder
.. code:: python

    # Sample Example to Showcase Working of Tree and its functions defined so far
    # ( NOT IN TEXTBOOK )
    # Tree Example Diagram @ http://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Binary_tree.svg/300px-Binary_tree.svg.png
    
    # Defining Height = 0 Nodes ( Leafs ):
    
    h0_1 = TreeNode(None, 5, None)
    h0_2 = TreeNode(None, 11, None)
    h0_3 = TreeNode(None, 4, None)
    
    # Defining Height = 1 Nodes ( Subtrees and one leaf - h1_1):
    
    h1_1 = TreeNode(None, 2, None)
    h1_2 = TreeNode(h0_1, 6, h0_2)
    h1_3 = TreeNode(h0_3, 9, None)
    
    # Defining Height = 2 Nodes ( Subtrees ):
    
    h2_1 = TreeNode(h1_1, 7, h1_2)
    h2_2 = TreeNode(None, 5, h1_3)
    
    # Defining Height = 3 Node ( root ):
    
    h3_1 = TreeNode(h2_1, 2, h2_2)
    
    tree1 = Tree(h3_1)
    
    print "inorder iteration using next() definition ( as provided in the TextBook )\n"
    
    for i in tree1:
        print i,
        
    print "\n\nInorderIterator using Generator function\n"
    
    for i in tree1.InorderIterator():
        print i, 
        
    print "\n\nPost order traversal using function Postorder()\n"
    
    tree1.Postorder()
    
    print "\n\nPre order traversal using function Preorder()\n"
    
    tree1.Preorder()
    
    print "\n\nIn order traversal using function Inorder()\n"
    
    tree1.Inorder()
    
    print "\n\nIn order traversal using function NonrecInorder()\n"
    
    tree1.NonrecInorder()
    
    print "\n\nLevel order traversal using function LevelOrder()\n"
    
    tree1.LevelOrder()

.. parsed-literal::

    inorder iteration using next() definition ( as provided in the TextBook )
    
    2 7 5 6 11 2 5 4 9 
    
    InorderIterator using Generator function
    
    2 7 5 6 11 2 5 4 9 
    
    Post order traversal using function Postorder()
    
    2 5 11 6 7 4 9 5 2 
    
    Pre order traversal using function Preorder()
    
    2 7 2 6 5 11 5 9 4 
    
    In order traversal using function Inorder()
    
    2 7 5 6 11 2 5 4 9 
    
    In order traversal using function NonrecInorder()
    
    2 7 5 6 11 2 5 4 9 
    
    Level order traversal using function LevelOrder()
    
    2 5 9 4 7 6 11 5 2


PROGRAM 5.8, PAGE 269
---------------------

.. code:: python

    # O(1) space inorder traversal
    
    def _NoStackInorder(self):
        # Inorder traversal of Binary Tree using a fixed amount of additional storage
        if self.root is None:
            return
    
        top = lastRight = p = q = r = r1 = None
        p = q = self.root
        while True:
            while True:
                if ( p.leftChild is None ) and ( p.rightChild is None ):
                    # Leaf Node
                    self.Visit(p)
                    break
    
                elif p.leftChild is None:
                    # Visit p and move to p.rightChild
                    self.Visit(p)
                    r = p.rightChild
                    p.rightChild = q
                    q = p
                    p = r
                
                else:
                    # move to p.leftChild
                    r = p.leftChild
                    p.leftChild = q
                    q = p
                    p = r
    
            # p is a leaf node move upward to a node whose right subtree has not yet been examined
            av = p
            while True:
                if p == self.root:
                    return None
    
                if q.leftChild is None:
                    # q is linked via rightChild
                    r = q.rightChild
                    q.rightChild = p
                    p = q
                    q = r
    
                elif q.rightChild is None:
                    # q is linked via leftChild
                    r = q.leftChild
                    q.leftChild = p
                    p = q
                    q = r
    
                    self.Visit(p)
    
                else:
                    # Check if p is a rightChild of q
                    if q == lastRight:
                        r = top
                        lastRight = r.leftChild
                        top = r.rightChild # unstack
                        r.leftChild = r.rightChild = None
                        r = q.rightChild
                        q.rightChild = p
                        p = q
                        q = r
    
                    else:
                        # p is leftChild of q
                        self.Visit(q)
                        av.leftChild = lastRight
                        av.rightChild = top
                        top = av
                        lastRight = q
                        r = q.leftChild
                        q.leftChild = p # Restore link to p
                        
                        r1 = q.rightChild
                        q.rightChild = r
                        p = r1
    
                        break
    
    Tree.NoStackInorder = _NoStackInorder
.. code:: python

    # Sample Output ( NOT IN TEXTBOOK )
    tree1.NoStackInorder()

.. parsed-literal::

    2 7 5 6 11 2 5 4 9


PROGRAM 5.9, PAGE 270
---------------------

.. code:: python

    # Copying a binary tree.
    
    # Overloading __init__ to provide copy constructor like functionality
    
    def _init(self, copy_from = None):
            # This implementation differs from the Textbook definition
            # Here Tree is an encapsulation of the root
            # root is a Binary Tree formed by the Linking together TreeNodes
            # This will avoid confusion between Tree and TreeNode
            """ Create a new Binary Tree """
            
            # if the copy_from is a Tree Class object
            if isinstance(copy_from, Tree):
                self.root = self.Copy(copy_from.root)
                
            # if the copy_from is a root ( TreeNode object )
            else:
                self.root = copy_from
                # This also copies None to root if passed
                
    Tree.__init__ = _init
    
    def _Copy(self, origNode):
        # Workhorse which recursively copies the whole binary tree.
        
        # Return a pointer to an exact copy of the binary tree rooted at origNode
        
        if origNode is None:
            return None
        
        return TreeNode(self.Copy(origNode.leftChild), origNode.data, self.Copy(origNode.rightChild))
    
    Tree.Copy = _Copy
PROGRAM 5.10, PAGE 270
----------------------

.. code:: python

    # Binary tree equivalence
    
    def _eq(self, t):
        if isinstance(t, Tree):
            return self.Equal(self.root, t.root)
    
    Tree.__eq__ = _eq
        
    def _Equal(self, a, b):
        # Workhorse which recursively checks for equivalence
        if (a is None) and (b is None):
            return True
        
        # Return True if :
            # Both a and b are not None
            # Data is same
            # left subtrees are equal
            # right subtrees are equal
        
        return ( a is not None ) and (b is not None ) and (a.data == b.data) and self.Equal(a.leftChild, b.leftChild) and self.Equal(a.rightChild, b.rightChild) 
        
    Tree.Equal = _Equal

.. code:: python

    # Sample Output ( NOT IN TEXT BOOK )
    
    tree2 = Tree(tree1) # Copy from tree1 to tree2
    tree2.NoStackInorder()
    
    print "\n\nBinary Tree Equivalence: ", tree2 == tree1
    
    tree3 = Tree(None) # Empty tree
    print "\n\nBinary Tree Equivalence 2: ", tree1 == tree3

.. parsed-literal::

    2 7 5 6 11 2 5 4 9 
    
    Binary Tree Equivalence:  True
    
    
    Binary Tree Equivalence 2:  False


PROGRAM 5.12, PAGE 273
----------------------

.. code:: python

    # Expression Tree definition ( NOT GIVEN IN THE TEXT BOOK )
    # This definition is not given in the text book but is assumed for the algorithm to work
    
    # Here the structure of TreeNode have been kept the same for ease of presentability of sample output
    # In the Text Book a different structure is presented with Nodes having twin data field
    
    class ExprTree(Tree):
        
        def evaluate(self, node = -1, variable_values = None):
            """ 
            Evaluates the Tree for the given list of variable values 
            
            USAGE:
            >>> t = ExprTree(root)
            >>> t.evaluate([1, 0, 0])
            1
            
            """
            # Exception handling
            if (node == -1) and (variable_values is None):
                raise Exception("Variable Value vector is not passed")
                
            # Initializing
            elif node == -1:
                node = self.root
            
            
            # PROGRAM 5.12, PAGE 273
            # Visiting a Node in an Expression Tree
            
            var_list = self.getVariables()
            
            # If the node contains boolean data
            if node.data in [1, 0]:
                return bool(node)
            
            # If the node contains a variable
            if node.data in var_list:
                var_index = var_list.index(node.data)
                var_value = variable_values[var_index]
                
                return bool(var_value)
            
            # If the node is an operator
            elif node.data in [ '^', 'v', '~' ]:
                
                if node.data == '^':
                    # And operator
                    return self.evaluate(node.rightChild, variable_values) and self.evaluate(node.leftChild, variable_values)
                elif node.data == 'v':
                    # Or operator
                    return self.evaluate(node.rightChild, variable_values) or self.evaluate(node.leftChild, variable_values)
                elif node.data == '~':
                    # Not operator
                    return not self.evaluate(node.rightChild, variable_values)
                
        def getVariables(self, node = -1):
            # Defining a static var_list for storage of variables while recursing throught the tree
                
            if node is -1:
                node = self.root
            
            if node == self.root:
                self.getVariables.__dict__["var_list"] = []
            
            if node is None:
                return
    
            # If the node contains a variable string and the variable is not already in the static var_list
            if ( node.data not in ['^', 'v', '~', 1, 0, True, False, None] ) and ( node.data not in self.getVariables.__dict__["var_list"] ):
                self.getVariables.__dict__["var_list"].append(node.data)
    
            self.getVariables(node.rightChild) # Parse the right subtree
            self.getVariables(node.leftChild) # Parse the left subtree
    
            var_list = sorted(self.getVariables.__dict__["var_list"])
            
            if node == self.root:
                # Cleaning up the function namespace if the function returns back to the root node
                self.getVariables.__dict__.pop('var_list')
            
            # Return the list of variables
            return var_list
    
    # SAMPLE OUTPUT - Refer Tree Diagram - Figure 5.18, Page 272
    
    # Constructing the Expression Tree
    
    # Defining leaf Nodes:
    
    l1   = TreeNode(None, 'x1', None)
    l2   = TreeNode(None, 'x2', None)
    l3   = TreeNode(None, 'x3', None)
    
    o1 = TreeNode(None, '~', l2)
    o2 = TreeNode(l1, '^', o1)
    o3 = TreeNode(None, '~', l1)
    o4 = TreeNode(o3, '^', l3)
    
    o5 = TreeNode(o2, 'v', o4)
    o6 = TreeNode(None, '~', l3)
    
    o7 = TreeNode(o5, 'v', o6)
    
    exp = ExprTree(o7)
    
    print "Inorder traversal : "
    exp.Inorder()
    
    print "\n\nThe variable list is : "
    print exp.getVariables()
    
    print "\nEvaluating the expression for (1,1,1) : ",
    print exp.evaluate(variable_values = [1, 1, 1])
    
    print "\nEvaluating the expression for (1,0,1) : ",
    print exp.evaluate(variable_values = [1, 0, 1])


.. parsed-literal::

    Inorder traversal : 
    x1 ^ ~ x2 v ~ x1 ^ x3 v ~ x3 
    
    The variable list is : 
    ['x1', 'x2', 'x3']
    
    Evaluating the expression for (1,1,1) :  False
    
    Evaluating the expression for (1,0,1) :  True


PROGRAM 5.11, PAGE 273
----------------------

.. code:: python

    # First version of satisfiability algorithm
    
    def _Satisfiability(self):
        var_list = self.getVariables()
        
        no_of_vars = len(var_list)
        
        for i in range(no_of_vars):
            
            # Convert an integer to a binary string
            # 5 --> '0b101' --> '101' --> '0101'
            binary_i = (bin(i)[2:]).zfill(no_of_vars)
            
            # Convert a binary string to a vector of binary data
            # "1111" --> ['1', '1', '1', '1'] --> [1, 1, 1, 1]
            input_vector = map(int, list(binary_i))
            
            if self.evaluate(variable_values = input_vector):
                print input_vector
                return True
            
        print "No satisfiable combination"
        return False
    
    ExprTree.Satisfiability = _Satisfiability
    
    # Sample Output
    exp.Satisfiability()

.. parsed-literal::

    [0, 0, 0]




.. parsed-literal::

    True



.. code:: python

    # Class Definition for ThreadedNode
    class ThreadedNode(TreeNode):
        def __init__(self):
            super(ThreadedNode, self).__init__()
            # Defining 2 new fields rightThread and leftThread
            self.rightThread = self.leftThread = None
            
    # Class Definition for ThreadedTree
    class ThreadedTree(ThreadedNode):
        def __init__(self):
            super(ThreadedTree, self).__init__()
PROGRAM 5.13, PAGE 277
----------------------

.. code:: python

    # Finding the inorder successor in a threaded binary tree
    def _ThreadedInorderIterator(self):
        """ Return the inorder successor of currentNode in a threaded binary tree """
        temp = currentnode.rightChild
        
        if currentNode.rightThread is None:
            while temp.leftThread is None:
                temp = temp.leftChild
        
        currentNode = temp
        
        if currentNode == root:
            return None
        else:
            return currentNode.data
        
    ThreadedTree.ThreadedInorderIterator = _ThreadedInorderIterator
PROGRAM 5.14, PAGE 279
----------------------

.. code:: python

    # Inserting r as the right child of s
    
    def _InsertRight(s, r):
        """ Insert r as the right child of s """
        r.rightChild = s.rightChild
        r.rightThread = s.rightThread
        r.leftChild = s
        r.leftThread = True # Left child is a thread
        s.rightChild = r
        s.rightThread = False
        if r.rightThread is None:
            temp = self.InorderSucc(r)
            # Returns the inorder successor of r
            temp.leftChild = r     
ADT 5.2, PAGE 280
-----------------

.. code:: python

    # A max priority queue
    
    # This defines the skeletal structure of a Max Priority Queue Class
    
    class MaxPQ(object):
        def __init__(self):
            pass
        def IsEmpty(self):
            # Returns true if the PQ is empty
            pass
        def Top(self):
            # Returns the reference to the max element ( Max priority queue top element )
            pass
        def Push(self):
            # Add an element to the priority queue
            pass
        def Pop(self):
            # delete element with max priority
            pass
        def __del__(self):
            # Distructor to delete reference to names that are no longer required
            pass
PROGRAM 5.15, PAGE 282
----------------------

.. code:: python

    # Max heap constructor
    class MaxHeap(object):
        def __init__(self, theCapacity = 10):
            if theCapacity < 1:
                raise Exception("Capacity must be >= 1")
    
            self.capacity = theCapacity
            self.heapSize = 0
            self.heap = dict()
            
        def IsEmpty(self):
            return ( self.heapSize == 0 ) or ( len(self.heap) == 0 )
PROGRAM 5.16, PAGE 285
======================

.. code:: python

    # Insertion into a max heap
    
    def _Push(self, e):
        """ Insert e into max heap """
        
        if self.heapSize == self.capacity:
            # Double the capacity
            self.capacity *= 2
            
        self.heapSize += 1
        currentNode = self.heapSize
        
        while ( currentNode != 1 ) and ( self.heap[currentNode/2] < e) :
            # Bubble up
            self.heap[currentNode] = self.heap[currentNode / 2] # Move parent down
            currentNode /= 2
            
        self.heap[currentNode] = e
        
    MaxHeap.Push = _Push
PROGRAM 5.17, PAGE 286
----------------------

.. code:: python

    # Deletion from a Max heap
    
    def _Pop(self):
        # Delete max element
        if self.IsEmpty():
            raise Exception("Heap is empty. Cannot delete")
            
    
    
        # Remove last element from heap
        self.heapSize -= 1
        lastE = self.heap[self.heapSize]
        
        # Tricle down
        currentNode = 1 # Root
        child = 2       # A child of the CurrentNode
        while child <= self.heapSize:
            # set child to larger child of currentNode
            if child < self.heapSize and self.heap[child] < self.heap[child+1]:
                child += 1
                
            if lastE >= self.heap[child]:
                # If lastE can be put in the currentNode, break out of the loop
                break
                
            # If not
                
            self.heap[currentNode] = self.heap[child]
            currentNode = child    # move child up
            child *= 2    # Move down a level
            
        self.heap[currentNode] = lastE
        
    MaxHeap.Pop = _Pop
.. code:: python

    # Sample Output - NOT IN TEXTBOOK
    # Refer Figure 5.26, Page 284
    
    a = MaxHeap()
    
    a.Push(20)
    a.Push(15)
    a.Push(10)
    a.Push(14)
    a.Push(2)
    a.Push(5)
    a.Pop() # 20 will be removed.
    
    print a.heap

.. parsed-literal::

    {1: 15, 2: 14, 3: 10, 4: 2, 5: 2, 6: 5}


ADT 5.3, PAGE 287
-----------------

.. code:: python

    # A dictionary
    
    class Dictionary:
        def __init__(self):
            pass
        
        def IsEmpty(self):
            pass
        
        def Insert(self, pair):
            pass
        
        def Delete(self, pair):
            pass
PAIR / BST CLASS DECLARATIONS
-----------------------------

.. code:: python

    # Pair Class - Key / Value pair ( data ) of a bst node
    class Pair(object):
        def __init__(self, key = None, value = None):
            self.first = key  # key
            self.second = value # value
        # To print the key value pairs when Pair is "print"-ed
        def __repr__(self):
            return "( " + str(self.first) + " , " + str(self.second) + " )"
        __str__ = __repr__
            
    # Abstract Class for the Binary Search Tree deriving from the Tree Class
    class BST(Tree):
        def __init__(self, *inputs):
            Tree.__init__(self, *inputs)
PROGRAM 5.18, PAGE 289
----------------------

.. code:: python

    # Recursive search of a binary search tree
    def _Get(self, frm, k):
        # Search binary search tree for a pair with key k
        # If such a pair is found, return a pointer to this pair, other wise return None
        
        # Driver
        if ( k is None ):
            k = frm
            return self.Get(self.root, k)
        
        # Workhorse
        if ( frm is None ):
            return None
        
        
        if ( k < frm.data.first ):  # TreeNode will have Pair object as its data attribute
            return self.Get(frm.leftChild, k)
        
        elif ( k > frm.data.first ):
            return self.Get(frm.rightChild, k)
        
        else:
            return frm.data # Returns the pair object which is the frm - TreeNode's data attribute.
        
    BST.Get = _Get
PROGRAM 5.19, PAGE 290
----------------------

.. code:: python

    # Iterative search of a binary search tree.
    
    def _Get_Iterative(self, k):
        while ( currentNode is not None ):
            if ( k < currentNode.data.first ):  
                #NOTE: currentNode is a TreeNode object, data is a Pair object and first is the key of that Pair object.
                currentNode = currentNode.leftChild
            elif ( k > currentNode.data.first ):
                currentNode = currentNode.rightChild
            else:
                return currentNode.data
            
        # If there is no matching pair ( while loop terminates without returning )
        return None            
PROGRAM 5.20, PAGE 290
----------------------

.. code:: python

    # Searching the Binary Search Tree by rank
    def _RankGet(self, r):
        # Search the binary search tree for the rth smallest pair
        while ( currentNode is not None ):
            if ( r < currentNode.leftSize ):
                currentNode = currentNode.leftChild
                
            elif ( r > currentNode.leftSize ):
                r -= currentNode.leftSize
                currentNode = currentNode.rightChild
                
            else:
                return currentNode.data
            
    BST.RankGet = _RankGet
PROGRAM 5.21, PAGE 292
----------------------

.. code:: python

    # Insertion into a binary search tree
    def _Insert(self, thePair):
        # Insert thePair
        # Search for thePair.first, pp is the parent of p
        p = self.root
        pp = None
        
        while (p is not None):
            pp = p
            if ( thePair.first < p.data.first ):
                p = p.leftChild
            elif ( thePair.first > p.data.first ):
                p = p.rightChild
            else:
                # Duplicate, Update associated element
                p.data.second = thePair.second
                return None
            
        # Perform the insertion
        p = TreeNode(data = thePair)
        if ( self.root is not None ):
            if ( thePair.first < pp.data.first ):
                pp.leftChild = p
            else:
                pp.rightChild = p
        else:
            root = p
            
    BST.Insert = _Insert
PROGRAM 5.22, PAGE 295
----------------------

.. code:: python

    # Splitting a Binary Search Tree
    def _Split(self, k, small, mid, big):
        """
        The Binary Search Tree is split into 3 subtrees - small, mid and big
        small is the BST with all the keys less than k
        big is the BST with all the keys greater than k
        mid is the Pair object with key equal to k ( if any such pair exists in BST )
        """
        # Split the Binary Search Tree with respect to the key k
        
        # Empty tree :
        if ( self.root is None ):
            small.root = big.root = None
            return
        
        sHead = TreeNode()
        s = sHead
        bHead = TreeNode()
        b = bHead
        currentNode = self.root
        
        while ( currentNode is not None ):
            if ( k < currentNode.data.first ):
                # Add it to the big
                b.leftChild = currentNode
                b = currentNode
                currentNode = currentNode.leftChild
            elif ( k > currentNode.data.first ):
                # Add it to the small
                s.rightChild = currentNode
                s = currentNode
                currentNode = currentNode.rightChild
            else:
                # Split at the currentNode
                s.rightChild = currentNode.leftChild
                b.leftChild = currentNode.rightChild
                small.root = sHead.rightChild
                del sHead
                big.root = bHead.leftChild
                del bHead
                mid.first = currentNode.data.first; mid.second = currentNode.data.second
                del currentNode
                return
            
            # No pair with key k
            s.rightChild = b.leftChild = None
            small.root = sHead.rightChild
            del sHead
            big.root = bHead.leftChild
            del bHead
            mid = None
            return
        
    BST.Split = _Split
.. code:: python

    # Example problem on BST ( NOT IN TEXTBOOK )
    
    node_2  = TreeNode(None, Pair(2,"Two"), None) 
    # Here 2 is the key and "Two" is the value of the Pair object
    # Which forms the data of the TreeNode object
    node_5  = TreeNode(node_2, Pair(5,"Two"), None)
    
    node_80 = TreeNode(None, Pair(80, "Eighty"), None)
    node_40 = TreeNode(None, Pair(40, "Forty"), node_80)
    
    # Root node
    node_30 = TreeNode(node_5, Pair(30, "Thirty"), node_40)
    
    bst_1 = BST(node_30)
    
    print "The Inorder traversal of the bst before Insert : "
    bst_1.Inorder()
    
    bst_1.Insert(Pair(35, "Thirty Five"))
    
    print "\n\nThe Inorder traversal of the bst after Inserting : "
    bst_1.Inorder()

.. parsed-literal::

    The Inorder traversal of the bst before Insert : 
    ( 2 , Two ) ( 5 , Two ) ( 30 , Thirty ) ( 40 , Forty ) ( 80 , Eighty ) 
    
    The Inorder traversal of the bst after Inserting : 
    ( 2 , Two ) ( 5 , Two ) ( 30 , Thirty ) ( 35 , Thirty Five ) ( 40 , Forty ) ( 80 , Eighty )


.. code:: python

    # Ilustration of splitting the tree :
    print "Splitting the tree with key k = 30"
    print "--------------------------------------"
    small_subtree = BST()
    mid_pair = Pair()
    big_subtree = BST()
    bst_1.Split(30, small_subtree, mid_pair, big_subtree )
    
    print "\nThe small_subtree ( Inorder traversal ) is : "
    small_subtree.Inorder()
    
    print "\n\nThe mid_pair ( key, value ) is : "
    print mid_pair
    
    print "\n\nThe big_subtree ( Inorder traversal ) is : "
    big_subtree.Inorder()

.. parsed-literal::

    Splitting the tree with key k = 30
    --------------------------------------
    
    The small_subtree ( Inorder traversal ) is : 
    ( 2 , Two ) ( 5 , Two ) 
    
    The mid_pair ( key, value ) is : 
    ( 30 , Thirty )
    
    
    The big_subtree ( Inorder traversal ) is : 
    ( 35 , Thirty Five ) ( 40 , Forty ) ( 80 , Eighty )


PROGRAM 5.23, PAGE 307
----------------------

.. code:: python

    # Class definition and constructor for sets
    class Sets(object):
        def __init__(self, numberOfElements):
            if ( numberOfElements < 2 ):
                raise Exception("Must have at least 2 elements")
            self.n = numberOfElements
            self.parent = [-1]*n
PROGRAM 5.24, PAGE 308
----------------------

.. code:: python

    # Simple functions for union and find
    def _SimpleUnion(self, i, j):
        # Replace the disjoint sets with roots i and j, i != j with their union
        self.parent[i] = j
    
    Sets.SimpleUnion = _SimpleUnion
        
    def _SimpleFind(self, i):
        while ( parent[i] >= 0 ):
            i = parent[i]
        return
    
    Sets.SimpleFind = _SimpleFind
PROGRAM 5.26, PAGE 313
----------------------

.. code:: python

    # Collapsing Rule
    def _CollapsingFind(self, i):
        # Find the root of the tree containing element i,
        # Use the collapsing root rule to calculate all nodes from i to the root
        r = i
        while sellf.parent[r] >= 0:
            r = parent[r]
            
        while i != r:
            # Collapse
            s = parent[i]
            parent[i] = r
            i = s
            
        return r