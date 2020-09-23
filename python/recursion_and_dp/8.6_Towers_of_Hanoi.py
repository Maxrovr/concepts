def print_tower():
    for i in range(n):
        src = a[i] if len(a) > i else ''
        spr = b[i] if len(b) > i else ''
        dst = c[i] if len(c) > i else ''
        print(f'{src}\t{spr}\t{dst}')
    print("|-------|-------|")
    print("A       B       C\n")
    
def towers_of_hanoi(num_disks, source, dest, spare):
    if num_disks == 1:
        dest.append(source.pop())
        print_tower()
        return
    towers_of_hanoi(num_disks-1, source, spare, dest)
    dest.append(source.pop())
    print_tower()
    towers_of_hanoi(num_disks-1, spare, dest, source)

a = [1,2,3]
b = []
c = []
n = 3
print_tower()
towers_of_hanoi(n, a, b, c)