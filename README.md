# Tech Interview Concepts
A repository for all concepts I am learning. I am currently following *Gayle Laakmann McDowell's* `Cracking The Coding Interview`. You can too!

Check out my [website](https://rakshithsm.com) and [blog](https://rakshithsm.com/blog) for more.

## The story so far..
1. Sorting ([Cheat Sheet](https://github.com/Maxrovr/concepts/blob/master/theory/sorting.md))
    1. [Merge Sort](https://github.com/Maxrovr/concepts/blob/master/python/sorting/merge_sort.py) ([Original](https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/))
    2. [Quick Sort](https://github.com/Maxrovr/concepts/blob/master/python/sorting/quick_sort.py) ([Original](https://www.interviewbit.com/tutorial/quicksort-algorithm/))
    > :trophy:I highly recommend sketching out the sorting process on paper for multiple examples

2. Recursion and Dynamic Programming(DP)
    1. A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs. ([Solution](https://github.com/Maxrovr/concepts/blob/master/python/recursion_and_dp/8.1_Triple_Step.py))
    2. Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right. (1's in the grid are "navigable" and 0's are not) ([Solution](https://github.com/Maxrovr/concepts/blob/master/python/recursion_and_dp/8.2_Robot_In_A_Grid.py))
    3. The classic Towers of Hanoi -  you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle tarts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
        1. Only one disk can be moved at a time.
        2. A disk is slid off the top of one tower onto another tower.
        3. A disk cannot be placed on top of a smaller disk.
    Write a program to move the disks from the first tower to the last using stacks. ([Solution](https://github.com/Maxrovr/concepts/blob/master/python/recursion_and_dp/8.6_Towers_of_Hanoi.py))

3. Graphs and Trees
    1. Inorder Traversal - Go **Left**, then the **current node** and then go **Right**
        1. Recursive - Trivial solution
        2. [Iterative](https://github.com/Maxrovr/concepts/blob/master/python/graphs_and_trees/inorder_iterative.py)

4. [Object Oriented Programming - SOLID Principles](https://github.com/Maxrovr/concepts/blob/master/theory/SOLID_Principles.md)
