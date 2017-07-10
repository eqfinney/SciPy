#
# SciPy Teen Track Morning Session
# Part 2 (After Break)
# Emily Quinn Finney
#

# Introduction
"""
So now we're familiar with a lot of different forms that our data could take,
that is, our data types. Can people give me examples? (Int, list, float, set,
dict, string, tuple.) Now that we know what those forms are, we're going to
spend some time this session getting acquainted with how to use those forms.
We'll also practice using packages that contain even more operations on our
data types. 
"""

# Some cool things about tuples, lists, sets, and dicts
# Time estimate: 20 min
"""
Now let's learn some cool properties of lists, sets, and dicts. Turns out
you can change values in a list, set or dict with certain commands. We'll
use an example from the IMDB database. 
"""

# showing off list capabilities
items = ['cat', 'dog', 'pet', 'bird', 'reptile']
print(items)
items[2] = 'spider'
print(items)
del items[2]
print(items)
items.append('frog')
print(items)
items.sort()
print(items)

# showing off set capabilities
items = {'cat', 'dog', 'pet', 'bird', 'reptile', 'cat'}
print(items)
items.add('spider')
print(items)
items.remove('reptile')
print(items)
print('bird' in items)

# showing off dict capabilities


# Importing packages
# Time estimate: 10 min
"""
There are also outside packages that do even cooler operations on lists, sets,
and dicts. A package is a collection of Python operations that go above and
beyond what you might use in every program. For instance, I may not need to
calculate a square root every day. But if I do, I can use the math package.
"""
import math
print(math.sqrt(9))

"""
If I don't want to type a long name in front of my function every time I use
it, I can do this:
"""
from math import sqrt
print(sqrt(9))

"""
If I always want to know where my package comes from, here's another thing
I can do:
"""
import math as m
print(m.sqrt(9))

"""
Or:
"""
from math import sqrt as sq
print(sq(9))

"""
Here's some other cool packages. Have them do examples with random.
"""


# Iterations, reductions, and comprehensions
# Time estimate: 30 min
"""
So now that we've got types down, I'd like to start using more interesting
examples. I pulled this movie name from the Internet Movie DataBase (IMDB).
We'll spend a bunch more time with the IMDB database later.
"""

# iterations
"""
You'll notice these may remind you a lot of for loops!
"""
names = ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi']
for name in names:
    print "Star Wars: " + name

names = ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi']
for num, name in enumerate(names):
    print "Star Wars: Episode " + str(num + 4) + ": " + name

names = ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi']
episodes = ['IV', 'V', 'VI']
for num, name in zip(episodes, names):
    print "Star Wars: Episode " + str(num) + ": " + name


# reductions
budgets = [35000000, 32000000, 780000000, 28000, 39848000]
total_budget = sum(budgets)
print(total_budget)
min_budget = min(budgets)
print(min_budget)
max_budget = max(budgets)
print(max_budget)

"""
Have them practice, with examples. Maybe have them use an example with a dict.
"""

# comprehensions
values = [1, 2, 3, 4, 5, 6]
print(values)
squares = [ x*x for x in values if (x != 5)]
print(squares)

values = {1, 2, 3, 4, 8, 9, 2}
print(values)
squares = { x*x for x in values if (x != 5)}
print(squares)


"""
This gives us a lot of great tools to work with! Armed with these ways of
storing and manipulating our data, we can understand what is in a database
and start doing real data analysis. In the afternoon, we will introduce
two helpful packages, NumPy and matplotlib. We will learn how to read in
a database file and plot the information inside it. We will also learn how
to write a function, which will help us be able to repeat a data analysis
procedure even when our data are different.
"""
