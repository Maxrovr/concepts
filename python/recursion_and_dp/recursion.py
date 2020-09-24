def fib(n):
    """Returns the nth element of the fibonacci sequence"""
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_dp(n):
    m = [0] * (n + 1)
    m[1] = 1
    def helper(n, m):
        if n == 0 or n == 1:
            return m[n]
        if m[n] == 0:
            m[n] = helper(n-1, m) + helper(n-2, m)
        return m[n]
    return helper(n, m)

print(fib(6))
print(fib_dp(6))