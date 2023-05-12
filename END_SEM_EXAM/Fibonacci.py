# Iterative:
def fibonacci_iterative(n):
    if n <= 1:
        return n
    
    fib = [0, 1]
    
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib[n]
# Recursive:
def fibonacci_recursive(n):
    if n <= 1:
        return n
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
"""
The recursive algorithm for computing Fibonacci numbers has an exponential time complexity of O(2^n), where n is the input number.
This is because each recursive call branches into two more recursive calls, resulting in an exponentially increasing number of function calls.

On the other hand, the iterative algorithm has a linear time complexity of O(n), where n is the input number. 
This is because each iteration of the loop involves only a few basic arithmetic operations, resulting in a linear number of operations.

Therefore, the iterative algorithm is much more efficient than the recursive algorithm for large values of n, 
as the latter quickly becomes unfeasible due to the large number of function calls required.
"""
