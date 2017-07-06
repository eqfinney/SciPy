#
# SciPy Teen Track Morning Session
# Part 1 (Before Break)
# Emily Quinn Finney
#

# Introduction
# Time estimate: 10 min
"""
Today we are going to review the basics of Python, including some of its
special built-in objects. We will also study other SciPy packages useful
for data analysis. These include NumPy ("Numerical Python"), which helps
analyze numerical data with many-dimensional tables called arrays, and
matplotlib ("Matlab Plot Library"), which helps visualize data with various
plotting tools. We will go through examples of Python code, as well as
write our own scripts. At the end of the day, we will do a mini-analysis
that puts all those skills together.

We will have a morning session and an afternoon session, each of which
will have a fifteen-minute break in the middle. Bathrooms are located _,
and please no eating and drinking in the conference room(?).

Here's our tentative schedule:
9am-10:30am   Introduction to Jupyter Notebooks. Introduction to basic
              Python syntax (data types, if/else statements, for/while
              loops, indexing, string slicing). 

10:45am-12pm  Introduction to more advanced data types (dictionaries,
              lists, sets) and their functionality. Introduction to
              importing packages. Brief introduction to NumPy. 

1:30pm-3pm    Introduction to functions. Introduction to matplotlib.
              We'll start to learn what's cool in our IMDB data by
              making plots of movie popularity.

3:15pm-5pm    Mini-analysis of the IMDB data set.


I have given each person a green post-it note and a red post-it note. As
we are going through the material, if you have finished the tutorial task,
put up your green post-it note to let me know. If you are confused about
the task, put up your red post-it note. In addition, if you have a question
or for any reason want to talk to someone about the tutorial material, feel
free to raise your hand to ask me or one of the tutorial volunteers for
assistance. That's what we're here for!
"""

# Introduction to Jupyter Notebooks.
# Time estimate: 10 min


# Introduction to basic Python syntax
"""
Many of you are already familar with the basic syntax of Python. But we're
going to spend this first section reviewing, to make sure everyone is on
the same page for later in the day. I learned some new stuff about Python
while preparing for this tutorial, so even if you are already familiar
with basic Python syntax be on the lookout for cool new tidbits! Again, if
you feel lost or stuck, put up a red post-it note or raise your hand. I
and the tutorial volunteers are happy to help.
"""

# Data types
# Time estimate: 20 min
# ints, floats, booleans (won't mention long, complex)
"""
If you've used a programming language before, you are probably familiar
with some of the objects you can use to communicate with your computer.
"""
2.0
print(type(2.0))

2
print(type(2))

True
print(type(True))


# strings, tuples, lists, sets (won't mention bytes, byte arrays, frozen sets)
"""
There are also non-numerical objects.
"""
"Hi scipy"
print(type("Hi scipy"))

(1,2,3)
print(type((1,2,3)))

('h','i',' ','s','c','i','p','y')
print(type(('h','i',' ','s','c','i','p','y')))

[1,2,3]
print(type([1,2,3]))

['h','i',' ','s','c','i','p','y']
print(type(['h','i',' ','s','c','i','p','y']))

{1,2,3}
print(type({1,2,3}))

{'h','i',' ','s','c','i','p','y',}
print(type({'h','i',' ','s','c','i','p','y',}))

# dicts
# discuss key/value pairs
actors = {"Batman Begins": "Clark Gable", "The Last Jedi": "Mark Hammill"}
print(actors["The Last Jedi"])

"""
Here have them do a few minutes of examples with types, perhaps involving
the Davis farmers' market because that is ridiculous.
"""


# Indexing/slicing and if/else
# Time estimate: 20 min
"""
So now that we've got types down, I'd like to start using more interesting
examples. I pulled this movie name from the Internet Movie DataBase (IMDB).
We'll spend a bunch more time with the IMDB database later.
"""

# assigning variables
movie_title = "Batman Begins"
print(movie_title)
print(type(movie_title))

# indexing
movie_title[0]
print(movie_title[0])

movie_title[1]
print(movie_title[1])

movie_title[-1]
print(movie_title[-1])

# slicing (introduce len)
print(movie_title[:6])

# if/else
# create a more introductory example
answer = input("What is your favorite animal?")
length = len(answer)
if answer[length:] == "at":
    print("Your favorite movie must be " + str(answer) + "man!")
elif answer == "spider":
    print("Your favorite movie must be " + str(answer) + "man!")
else:
    print("I don't think you even like movies.")

"""
Have them practice, with examples.
"""


# String manipulation and loops
# Time estimate: 20 min
"""
Here are some more tools for creating and changing strings. Also loops.
"""
# string manipulation
print(movie_title[:6].upper() + movie_title[7:].lower())
print(movie_title.split())

# while and while/else loops
count = 0
while count < 26:
    print("NA ")
else:
    print(movie_title[:6].upper() + "!")


# for and for/else loops
animals = ["bat", "cat", "gnat", "rat"]
for creature in animals:
    print "I love " + str(creature) + "man!"

# and include a less trivial example

"""
Have them practice with a different set of examples.
"""


"""
That's all we'll go over for now. In the next section, we'll talk about
how to add and remove items from sets, lists, and dictionaries. We'll talk
about how to make dicts with more than one value per key, and how to use
those dicts. And we'll talk about how to import packages, which gives us
many more tools for understanding our data.
"""
