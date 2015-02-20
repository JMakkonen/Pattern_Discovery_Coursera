# Pattern_Discovery_Coursera
Python implementation of discussed algorithms

This repo has been set up to capture and share some stuff arising from the Pattern Discovery course.
IMHO, the course should really have a coding component/exercises to it.  I am not very happy with this course, the course forums also have many people expressing frustration.

Anyway, see file P1026.py for some callable functions that are the basic starting items for
building a version of the apriori algorithm for finding frequent patterns in data.
There are 2 slightly useful functions included in the file.
all_subsets(S) where S is a set, returns a list of all of the subsets of S including the original set.
proper_subsets(S) where S is a set, returns a list of all of the proper subsets and uses the all_subsets() function above.

If anyone can explain to me why you are not allowed to put sets into a set, I would appreciate that.  It gives hash errors.
Seriously, why can you not have a set such as { {1,2}, {3,4}, {3}}?

Plans for the future include creating a fully functioning call library for the apriori and other 
algorithms mentioned in the course lectures.
