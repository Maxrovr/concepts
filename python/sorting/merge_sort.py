class MergeSort:
    def _merge(self, a, start, mid, end):
        """Merges 2 arrays (one starting at start, another at mid+1) into a new array and then copies it into the original array"""
        # Start of first array
        s1 = start
        # Start of second array
        s2 = mid + 1
        # The partially sorted array
        s = []
        # for - till we iterate over all elements of partial array being sorted
        for i in range(end - start + 1):
            # If second array has been completely been traversed - first one still has some elements left - copy them all
            if s1 > mid:
                s.append(a[s2])
                s2 += 1
            # Vice-Versa
            elif s2 > end:
                s.append(a[s1])
                s1 += 1
            # Actual sorting - change symbols (either hardcode or dynamically with a bool descending)
            elif a[s1] <= a[s2]:
                s.append(a[s1])
                s1 += 1
            # Vice-Versa
            else:
                s.append(a[s2])
                s2 += 1
        
        # Copy partially sorted array into original array
        a[start:end+1] = s

    def _merge_sort(self, a, start, end):
        """Divides array into halves and calls merge on them"""
        if start < end:
            mid = start + (end - start) // 2
            self._merge_sort(a, start, mid)
            self._merge_sort(a, mid + 1, end)
            self._merge(a, start, mid, end)

    def merge_sort(self, a):
        self._merge_sort(a, 0, len(a) - 1)

a = [i for i in range(8,0,-1)]
print(f'Before: {a}')
obj = MergeSort()
obj.merge_sort(a)
print(f'After: {a}')

a = [i for i in range(7,0,-1)]
print(f'Before: {a}')
obj = MergeSort()
obj.merge_sort(a)
print(f'After: {a}')

a = [i for i in range(1,9)]
print(f'Before: {a}')
obj = MergeSort()
obj.merge_sort(a)
print(f'After: {a}')

a = [i for i in range(1,8)]
print(f'Before: {a}')
obj = MergeSort()
obj.merge_sort(a)
print(f'After: {a}')