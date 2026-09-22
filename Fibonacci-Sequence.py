# Generate a list containing the first n numbers of the Fibonacci sequence using loops or recursion
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
a = int(input("Enter the number of Fibonacci numbers to generate: "))
print("Fibonacci sequence:", fibonacci(a))