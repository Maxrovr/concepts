# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

# Recursive Solution
    # For the recursive solution, imagine a top down approach. The child is at the last step. It can get there from (n-1 st step and then a single step) or (n-2 nd step and take the 2 step) or (n-3 rd step and take the 3 step) [The paranthesis are for readbility]. This translates into `recursive(n-1) + recursive(n-2) + recursive(n-3)`
    # So, for the base cases, we need to think of what happens if we hit the negative realm. Well, thats a 0. `if n < 0: return 0`
    # Simple. Things get a little mucky when we need to write for n = 0, Depending on where the child starts .i.e at n = 0 or n = 1, we need to make that case return a 1. If the child starts at step 0(n=0), then our base case will be `if n == 0: return 1`. But if this child starts at step 1(n=1): `if n <= 0: return 0` and `if n == 1: return 1`
# Recursive Solution with Memoization
    # Same as above, except create an array that holds already seen values, if not seen, add it to the array to make it seen.
# DP Solution
    # Coming soon

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
