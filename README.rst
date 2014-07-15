Data Structures By Horowitz - As iPython Notebooks
==================================================

About
-----

Python implementation of the examples in the text book `Fundamentals of
Data Structures in C++ by E.Horowitz, S.Sahni and
Mehta <http://www.amazon.in/dp/8173716064/ref=cm_sw_r_tw_dp_P0I9sb188T11M>`__.
This is a part of my contribution to the textbook companionship project
organized by the `FOSSEE <http://python.fossee.in/>`__ initiative of
`IIT Bombay <https://www.iitb.ac.in/>`__


Sample - Heap Sort : Refer - FIGURE 7.7, PAGE 416
-------------------------------------------------


.. parsed-literal::

    The input array ( Represented as dictionary ) : 
    {1: 26, 2: 5, 3: 77, 4: 1, 5: 61, 6: 11, 7: 59, 8: 15, 9: 48, 10: 19}



.. image:: Chapter%207/output_42_1.png


.. parsed-literal::

    Heap representation using the MaxHeap data structure ( Chapter 5 ): 
    {1: 77, 2: 61, 3: 59, 4: 48, 5: 19, 6: 11, 7: 26, 8: 1, 9: 15, 10: 5}



.. image:: Chapter%207/output_42_3.png



.. image:: Chapter%207/output_42_4.png


.. parsed-literal::

    Sorted :  [77]



.. image:: Chapter%207/output_42_6.png


.. parsed-literal::

    Sorted :  [77, 61]



.. image:: Chapter%207/output_42_8.png


.. parsed-literal::

    Sorted :  [77, 61, 59]



.. image:: Chapter%207/output_42_10.png


.. parsed-literal::

    Sorted :  [77, 61, 59, 48]



.. image:: Chapter%207/output_42_12.png


.. parsed-literal::

    Sorted :  [77, 61, 59, 48, 26]



.. image:: Chapter%207/output_42_14.png


.. parsed-literal::

    Sorted :  [77, 61, 59, 48, 26, 19]



.. image:: Chapter%207/output_42_16.png


.. parsed-literal::

    Sorted :  [77, 61, 59, 48, 26, 19, 15]



.. image:: Chapter%207/output_42_18.png


.. parsed-literal::

    Sorted :  [77, 61, 59, 48, 26, 19, 15, 11]



.. image:: Chapter%207/output_42_20.png


.. parsed-literal::

    Sorted :  [77, 61, 59, 48, 26, 19, 15, 11, 5]
    The final sorted array is :  [77, 61, 59, 48, 26, 19, 15, 11, 5, 1]


Installation and Dependencies
-----------------------------

The python codes are written in `IPython
Notebooks <http://ipython.org/notebook.html>`__ Version 2.0 -
Development Build as on Jan 2014:

To install ipython in debian based systems like Debian:

::

    sudo apt-get install ipython-notebook

To install ipython in Fedora 18 and Newer:

::

    sudo yum install python-ipython-notebook

To check version:

::

    ipython --version

If the version is not 2.0, `use the development
build <https://github.com/ipython/ipython>`__

Clone the repo:

::

    git clone --recursive https://github.com/ipython/ipython.git

Move into the directory

::

    cd ipython

Do a system wide install :

::

    sudo python setup.py install

Matrix Operations are carried out via Numpy libraries. To get the Scipy
libraries (which include numpy):

::

    sudo apt-get install python-scipy

or

::

    sudo yum install python-scipy

Once all the packages and dependencies are installed.

Clone the repository and move into it:

::

    git clone https://github.com/rvraghav93/Data-Structures-By-Horowitz-in-Python.git DataStructPy
    cd DataStructPy

Move into the required chapter (Replace N by chapter number):

::

    cd Chapter\ N

Run IPython Notebook

::

    sudo ipython notebook

For more help on IPython notebook try `this official
documentation <http://ipython.org/ipython-doc/stable/interactive/notebook.html>`__.

Contribute
----------

If you wish to contribute too, visit `FOSSEE <http://fossee.in/>`__ and
see if you can find anything matching your interests.

Copyright
---------

The copyrights for all the codes belong to the FOSSEE Department of IIT
Bombay.

Contact
-------

For any queries or help feel free to contact me at:

IRC: rvraghav93

GMail: rvraghav93@gmail.com

About Me:
---------

I am Raghav RV, an Undergrad student of Anna University interested in
FOSS, python, C++, computer vision, big data etc...
