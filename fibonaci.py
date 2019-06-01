calls = {}
def fib(n):
    if n in calls: 
        return calls[n]
    if n < 2: 
        calls[n] = n
        return n
    calls[n] = fib(n-1) + fib(n-2)
    return calls[n]

print([fib(n) for n in range(16)])