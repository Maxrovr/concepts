def partition(a, start, end):
    """Returns the index of the pivot element after inserting it in its right index"""
    # Chooses a pivot element and puts it in its place by pushing all elements smaller than pivot to one part of the array 
    # and all elements greater to another. These parts themselves are not yet sorted, but, trust me, they will be, soon...., very soon

    # i tracks the position where the pivot needs to be inserted once the for loop that shifts elements is completed
    i = start - 1
    
    # Pivot can be chosen as on of the following :
    # 1. Always pick first element as pivot.
    # 2. Always pick last element as pivot 
    # 3. Pick a random element as pivot.
    # 4. Pick median as pivot.
    
    # I have gone for the more traditional last element (which gives a horrible O(n^2) time complexity when array is already sorted)
    # for the more sophisticated random element as pivot call the rand_partition instead
    pivot = a[end]
    for j in range(start, end):
        if a[j] <= pivot:
            i += 1
            a[i],a[j] = a[j], a[i]
    # Put the pivot in its correct index .i.e 
    a[i + 1], a[end] = a[end], a[i + 1]
    return i + 1

def quick_sort(a, start, end):
    # Recursion base condition, same as merge sort
    if start < end:
        pi = partition(a, start, end)
        # I told you to trust me. This is where you split the array (logically, not physically. Duh!) using start (start of smaller part), pi (pi - 1 is the end of smaller part, pi + 1 is the start of larger part), and end(end is the end of smaller part). 
        # Then sort them recursively until only one remains (you know, By the rule of the arena, "Two elements enter, only one element leaves.")
        quick_sort(a, start, pi - 1)
        quick_sort(a, pi + 1, end)
    
cases = [[1,2,3,4,5],[1,2,3,4,5,6],[5,4,3,2,1],[5,4,3,2,1,0],[10,1,9,2,8,3]]
for case in cases:
    expected = sorted(case)
    quick_sort(case, 0, len(case) - 1)
    assert expected == case

from random import randint
def rand_partition ( a, start , end ):
    # Chooses position of pivot randomly by using rand() function .
    random = randint(start, end)
    #swap pivot with 1st element.
    a[random] , a[start] = a[start], a[random]        
    #call the above partition function
    return partition(a, start, end)       