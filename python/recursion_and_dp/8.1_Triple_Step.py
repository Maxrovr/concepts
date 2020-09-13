# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

def triple_step_recursive(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return triple_step_recursive(n-1) + triple_step_recursive(n-2) + triple_step_recursive(n-3) 
# Runtime Analysis: each fn call makes 3 recursive calls - recursion tree grows at 3^n - O(3^n)
# Space Analysis: Stack space is used 3^n times - O(3^n)

def triple_step_dp_main(n):
    mem = [-1] * (n + 1) # Need n + 1 because we need to store the value of step n as well
    def triple_step_dp(n, mem):
        if n < 0: 
            return 0
        if mem[n] != -1:
            return mem[n]
        else:
            mem[n] = triple_step_dp(n-1, mem) + triple_step_dp(n-2, mem) + triple_step_dp(n-3, mem)
        return mem[n]
    mem[0] = 1
    return triple_step_dp(n, mem)
# Runtime Analysis: O(n) recursive calls
# Space Analysis: O(n) stack space and memoization array
