# A gentlemans sorting cheatsheet :smiling_imp:

### A list of sorting techniques and some basic information to choose the best sorting technique for a particular situation

|Sorting Technique   |Time Complexity|Space Complexity |Is Stable  |Is InPlace|   
|----------------    |---------------|---------------- |---------  |-----------|
|Bubble Sort         |Best => O(n), Worst & Average => O(n*n)|O(1)|True|True
|Selection Sort|Best & Worst & Average => O(n*n)|O(1)|False|True|
|Insertion Sort|Best => O(n) , Worst & Average => O(n*n)|O(1)|True|True
|Heap Sort|Best & Worst & Average => O(nLog(n))| O(1)| False | True|
|Counting Sort|Best & Worst & Average => O(n+k)|O(n+k)|False| True|
|Merge Sort| Best & Worst & Average => O(nLog(n))|O(n)|True|False|
|Quick Sort| Best => O(nLog(n)) , Worst => O(n*n)|O(n) |False| True|

|Sorting Technique |When to use   |Remarks |
|---------------- |-----------   |------- |
|Bubble Sort|1. If array is of small size 2. If array is of large size but nearly sorted|Easiest to implement|
|Selection Sort|1. If array is of small size 2. To minimise the number of swaps|Bubble sort has more number of swaps as compare to Selection sort but bubble sort has better best time complexity. It can also be implemented as stabaly. Selection sort makes O(n) swaps which is minimum among all sorting algorithms mentioned above.|
|Insertion Sort|1. If array is of small size and nearly sorted|Standard Libraray of C uses this algo when n becomes smaller than a threshold and for small size it is better than merge and quick sort becasue of low constant values and non recusive in nature.|
|Heap Sort|When the input array is large and stable sort is not required.| It always guaranteed to be O(nLog(n)) with constant space which solves the problem of overflow of address space of a process which may occur in merge and quick sort(recursive stack).|
|Merge Sort|1. When we don't have random access(linked list) [like we have in array] 2.When array is not to large.|Divide & Conquer|
|Quick Sort|1. It is prefered over merge sort for extremely large array 2.When you don't care about worst case complexity|Divide & Conquer|

### A quick comaprision between the two most common sorting techniques
|Comparer|Quick Sort|Merge Sort|
|----|----|----|
|Time|O(nLog(n)),O(n*n)|O(nLog(n))|
|Space|O(1)|O(n)|
|Advantage|When random access is there|When random access is costly(i.e Linked List)|
|Stability|Not Stable|Stable|
|In-Place|In-Place|Not-In-Place|
|Address Space Overflow Condition|Never Arises|May arise when array/list is extremely large|