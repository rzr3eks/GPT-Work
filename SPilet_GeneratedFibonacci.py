def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example: Print the first 10 numbers in the Fibonacci sequence
n = 10
result = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {result}")
