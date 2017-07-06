#
# SciPy Teen Track Afternoon Session
# Part 3 (Before Break)
# Emily Quinn Finney
#

# Introduction
"""
We're finally ready to start diving into our data set! We'll start this section
by reading in a text file containing a version of the IMDB data set and getting
to know some of its basic properties (using the data types and manipulation
tools we discussed earlier). Then we'll learn how to plot our data, so that
we can see trends visually. Finally, we'll talk about how to create a function
that will allow you to reproduce an analysis on a different set of data. 
"""

# Reading in the data set and very basic exploratory analysis
# Time estimate: 30 min
"""
We're going to start by reading in our data set and learning how to navigate
a big table of information, using the tools we've already seen.
"""

# importing the relevant data
import csv
imdb = list(csv.DictReader(open('imdb_table.csv')))

# also have them use a little NumPy
import numpy as np
imdb_num = np.loadtxt('imdb_numtable.txt')

"""
Have them poke around their own exploratory analysis of different questions.
"""


# Plotting/basic intro to matplotlib
# Time estimate: 30 min
"""
Now we've seen how 
"""
# I think we can just do numerical data here. Maybe histograms. Maybe.


"""
Have them practice, with examples.
"""


# Syntax for functions
# Time estimate: 30 min
"""
So we've just done some pretty cool plotting using a real data set. But it may
be frustrating to have to type the same commands over and over again whenever
you want to do an analysis. Even more importantly, in scientific contexts, if
you are comparing data sets, you need to analyze them exactly the same in order
to ensure that any differences you may find are due to differences in the data
and not due to differences in how you conducted the analysis. One tool that is
helpful for standardizing steps in your analysis is Python's functions. 
"""

for data[0] in imdb_num:
    data_times_ten = data[0]*10
    return data_times_ten

"""
Now we have a pretty useful set of tools for data analysis! We can read in our
data, plot our data, and write functions to reproduce our analyses for new
sets of data. We'll be implementing everything we've learned in the next
section, when we will be trying to answer a new set of questions with the
IMDB data set. 
"""
