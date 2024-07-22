
def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):

        if n <= 0: 
            return 0
        
        if n in cache:
            return cache[n]
        
        max_calculated_fibonacci = max(cache.keys())

        for i in range(max_calculated_fibonacci + 1, n + 1):
            cache[i] = fibonacci(i - 1) + fibonacci(i - 2)
        
        return cache[i]

    

    return fibonacci

fib = caching_fibonacci()
print(fib(10)) 
print(fib(15))