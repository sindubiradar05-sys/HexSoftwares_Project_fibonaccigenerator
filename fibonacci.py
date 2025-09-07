def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Main program
num = int(input("Enter how many Fibonacci numbers to generate: "))
result = fibonacci(num)
print("Fibonacci Series:",result)
