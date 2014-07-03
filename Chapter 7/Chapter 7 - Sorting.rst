
PROGRAM 7.1, PAGE 395
---------------------

.. code:: python

    # Sequential Search
    
    def SeqSearch( a, n, k ):
        # Search a[1:n] from left to Right. Return least i such that
        # The key of a[i] equals k. If there is no such i, return 0
        # NOTE: The indexing is done from 1 ( To comply with the textbook style )
        i = 0
        while ( i <= n ) and ( a[i] != k ):
            i += 1
        if ( i > n ):
            return 0
        else:
            return i
PROGRAM 7.2, PAGE 397
---------------------

.. code:: python

    # Verifying two lists using a sequential search
    
    def Verify1( l1, l2, n, m ):
        """
        Compares two unordered lists l1 and l2 of size n and m respectively.
        """
        marked = [False]*(m+1)
        for i in range (n+1):
            j = SeqSearch(l2, m, l1[i])
            if ( j == 0 ):
                print l1[i], " not in l2 "
            else:
                if ( l1[i] != l2[j] ):
                    # Satisfies 3rd condition ( Refer Page 396 )
                    print "Discrepancy in ", l1[i]
                marked[j] = True
                
        for i in range(m+1):
            if ( not marked[i] ):
                print l2[i], " not in l1. " # Satsfies 2nd Condition ( Refer Page 396 )
        
        del marked   
PROGRAM 7.4, PAGE 399
---------------------

.. code:: python

    # Insertion into a sorted list
    def Insert(e, a, i):
        """
        Insert e into the ordered sequence a[1:i] such that the 
        resulting sequence a[1:i+1] is also ordered
        The array a must have space allocated for at least i + 2 elements
        """
    
        a.__setitem__(0, e)
        while ( e < a[i] ):
            a.__setitem__(i+1, a[i]) # To make an inplace assignments
            i -= 1
            
        a.__setitem__(i+1, e)
PROGRAM 7.5, PAGE 400
---------------------

.. code:: python

    # Insertion Sort
    
    def InsertionSort(a, n):
        """
        Sort a[1:n+1] into non decreasing order
        """
        
        for j in range(2, n+1):
            temp = a[j]
            Insert(temp, a, j-1)
EXAMPLE 7.1, PAGE 400
---------------------

.. code:: python

    n = 5
    a = [None, 5, 4, 3, 2, 1] 
    # NOTE: The index-0 element is None to comply with the standards of the Book
    
    InsertionSort(a, 5)
    print a[1:n+1]

.. parsed-literal::

    [1, 2, 3, 4, 5]


EXAMPLE 7.2, PAGE 400
---------------------

.. code:: python

    n = 5
    a = [None, 2, 3, 4, 5, 1]
    # NOTE: The index-0 element is None to comply with the standards of the Book
    
    InsertionSort(a, 5)
    print a[1:n+1]

.. parsed-literal::

    [1, 2, 3, 4, 5]


PROGRAM 7.6, PAGE 402
---------------------

.. code:: python

    # Quick Sort
    def QuickSort(a, left, right, debug=False):
        """
        Sort a[left:right+1] into non decreasing order using quick sort algorithm
        """
        # a[left] is arbitrarily chosen as the pivot.
        # Variables i and j are used to partition the subarray so that at any time a[m] <= pivot
        # m < i and a[m] >= pivot, m > j. It is assumed that a[left] <= a[right + 1]
        
        if ( left < right ):
            if ( debug ):
                print a[1:], "\t", left, "\t", right # To show the working of quick sort step by step
            i = left
            j = right + 1
            pivot = a[left]
            
            while ( i < j ):
                i += 1
                while a[i] < pivot:
                    i += 1
                
                j -= 1
                while a[j] > pivot:
                    j -= 1
                    
                if i < j:
                    # Inplace swapping a[i] and a[j]
                    temp = a[i]
                    a.__setitem__(i, a[j])
                    a.__setitem__(j, temp)
                    
            temp = a[j]
            a.__setitem__(j, a[left])
            a.__setitem__(left, temp)
            
            QuickSort(a, left, j - 1, debug ) # Recursively call QuickSort for the left subarray
            QuickSort(a, j + 1, right, debug ) # Recursively call QuickSort for the right subarray
            
            # NOTE: debug is just to visualize the working of quick sort and is unnecessary for 
            # the working of the algorithm.
EXAMPLE 7.3, PAGE 402
---------------------

.. code:: python

    n = 10
    a = [None, 26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
    # NOTE: The index-0 element is None to comply with the standards of the Book
    
    QuickSort(a, 1 , 10)
    print a[1:n+1]

.. parsed-literal::

    [1, 5, 11, 15, 19, 26, 37, 48, 59, 61]


FIGURE 7.1, PAGE 403
--------------------

.. code:: python

    n = 10
    a = [None, 26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
    # NOTE: The index-0 element is None to comply with the standards of the Book
    
    print "The working of the quick sort algorithm :\n\n"
    print "\t\tArray             \tLeft\tRight "
    print "--------------------------------------------------------"
    QuickSort(a, 1 , 10, debug=True)
    print "\n\nThe final sorted array : "
    print a[1:n+1]

.. parsed-literal::

    The working of the quick sort algorithm :
    
    
    		Array             	Left	Right 
    --------------------------------------------------------
    [26, 5, 37, 1, 61, 11, 59, 15, 48, 19] 	1 	10
    [11, 5, 19, 1, 15, 26, 59, 61, 48, 37] 	1 	5
    [1, 5, 11, 19, 15, 26, 59, 61, 48, 37] 	1 	2
    [1, 5, 11, 19, 15, 26, 59, 61, 48, 37] 	4 	5
    [1, 5, 11, 15, 19, 26, 59, 61, 48, 37] 	7 	10
    [1, 5, 11, 15, 19, 26, 48, 37, 59, 61] 	7 	8
    
    
    The final sorted array : 
    [1, 5, 11, 15, 19, 26, 37, 48, 59, 61]


.. code:: python

    # Copy function for Merge operation
    
    def copy(list_src, start_pos, end_pos, list_dest, copy_to_pos ):
        """
        Copy list_src[start_pos : end_pos] to list_dest[copy_to_pos:]
        """
        while ( start_pos <= end_pos ):
            #print "in cpy - src:  ", list_src, start_pos, end_pos, " dest : ", list_dest, copy_to_pos
            # In place assignment
            list_dest.__setitem__(copy_to_pos, list_src[start_pos])
            # Increment copy_to_pos and start_pos
            copy_to_pos += 1
            start_pos += 1      
PROGRAM 7.7, PAGE 408
---------------------

.. code:: python

    # Merging two sorted lists
    def Merge(initList, mergedList, l, m, n):
        """
        Merge the sorted initList[l:m] and initList[m+1:n] into one single sorted list
        mergedList[1:n]
        """
        i1 = l; iResult = l; i2 = m+1 # i1, i2 and iResult are list positions
        
        # while neither input list is exhausted
        while ( i1 <= m and i2 <= n ):
            if initList[i1] <= initList[i2]:
                mergedList.__setitem__(iResult, initList[i1])
                i1 += 1
            else:
                mergedList.__setitem__(iResult, initList[i2])
                i2 += 1
            iResult += 1
            
        # Copy remaining records, if any, of first list
        copy(initList, i1, m, mergedList, iResult)
        copy(initList, i2, n, mergedList, iResult)
PROGRAM 7.8, PAGE 410
---------------------

.. code:: python

    # Merge Pass
    def MergePass(initList, resultList, n, s):
        """
        Adjacent pairs of sublists of size s are merged from
        initList to resultList. n is the number of records in initList
        """
        i = 1 # i is the first position in first of the sublists being merged
        
        while ( i <= ( n - 2*s + 1 ) ):
            Merge(initList, resultList, i, i + s - 1, i + 2 * s - 1)
            
            # Merge remaining list of size < 2*s
            i += 2*s
        
        if ( i + s - 1 ) < n :
            Merge(initList, resultList, i, i+s-1, n)
        else:
            copy(initList, i, n, resultList, i)
PROGRAM 7.9, PAGE 410
---------------------

.. code:: python

    # Merge Sort
    def MergeSort(a, n, debug = False):
        """
        Sort a[1:n] into non decreasing order using MergeSort algorithm
        """
        tempList = [None]*(n+1)
        
        # l is the length of the sublist currently being merged
        l = 1
        while ( l < n ):
            MergePass(a, tempList, n, l)
            if ( debug ):
                print tempList[1:]
            
            l *= 2
            MergePass(tempList, a, n, l)
            # Interchange role of a and empList
        
            l *= 2
            
            # debug is used to control printing of the list as it gets modified by the algorithm
            # This is to illustrate the working of merge sort algorithm step by step.
            if ( debug ):
                print a[1:]
            
        del tempList  
EXAMPLE 7.5, PAGE 409
---------------------

.. code:: python

    n = 10
    a = [None, 26, 5, 77, 1, 61, 11, 59, 15, 48, 19]
    # NOTE: The index-0 element is None to comply with the standards of the Book
    
    MergeSort(a, 10)
    print a[1:]

.. parsed-literal::

    [1, 5, 11, 15, 19, 26, 48, 59, 61, 77]


FIGURE 7.4, PAGE 409
--------------------

.. code:: python

    # Working of the MergeSort algorithm
    n = 10
    a = [None, 26, 5, 77, 1, 61, 11, 59, 15, 48, 19]
    # NOTE: The index-0 element is None to comply with the standards of the Book
    print "The initial unsorted list is : "
    print a[1:], "\n"
    MergeSort(a, 10, debug=True)
    print "\nThe final sorted list is : "
    print a[1:]

.. parsed-literal::

    The initial unsorted list is : 
    [26, 5, 77, 1, 61, 11, 59, 15, 48, 19] 
    
    [5, 26, 1, 77, 11, 61, 15, 59, 19, 48]
    [1, 5, 26, 77, 11, 15, 59, 61, 19, 48]
    [1, 5, 11, 15, 26, 59, 61, 77, 19, 48]
    [1, 5, 11, 15, 19, 26, 48, 59, 61, 77]
    
    The final sorted list is : 
    [1, 5, 11, 15, 19, 26, 48, 59, 61, 77]


PROGRAM 7.10, PAGE 412
----------------------

.. code:: python

    # Recursive Merge Sort
    def rMergeSort(a, link, left, right):
        """
        a[left:right] will be sorted in a non decreasing order 
        using Merge Sort algorithm and recursive function call
        """
        # a[left:right] is to be sorted, link[i] is initially 0 for all i
        # rMergeSort returns the index of the first element in the sorted chain
        
        if ( left > right ):
            return left
        
        mid = ( left + right ) / 2
        return ListMerge(a, link, 
                         rMergeSort(a, link, left, mid),
                         rMergeSort(a, link, mid+1, right))
    
    # The list merge function is defined in PROGRAM 7.11, PAGE 413
PROGRAM 7.11, PAGE 413
----------------------

.. code:: python

    # Merging sorted chains
    def ListMerge(a, link, start1, start2):
        """
        Function to merge two chain start1 and  start2 in array a.
        Returns the first position of the resulting chain that is linked 
        in nondecreasing order of key values.
        """
        # The sorted chains beginning at start1 and start2, respectively, are merged.
        # link[0] is used as a temporary header. Return start of merged chain
        iResult = 0 # Last record of result chain
        i1 = start1; i2 = start2
        while ( i1 and i2 ):
            if a[i1] <= a[i2]:
                link.__setitem__(iResult, i1)
                iResult = i1; i1 = link[i1]
            else:
                link[iResult] = i2
                iResult = i2
                i2 = link[i2]
        
        # Attach remaining records to result chain
        if ( i1 == 0 ):
            link.__setitem__(iResult, i2)
        else:
            link.__setitem__(iResult, i1)
            
        return link[0]
MAX HEAP DATA STRUCTURE
-----------------------


PROGRAM 7.13, PAGE 415
----------------------

.. code:: python

    # Adjusting a Max Heap