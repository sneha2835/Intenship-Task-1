# Program on Fibonacci Series - Task 1 of Internship
def fibonacci(n):  # Declare Function
    fib_series = [0, 1]  # Initialize Array with first two Fibonacci numbers
    while len(fib_series) < n:  # Use while loop to generate Fibonacci series up to n-th term
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]  # Return the first n elements of the Fibonacci series

n = 10  # Set n to 10
print(fibonacci(n))  # Print the function with n as an argument