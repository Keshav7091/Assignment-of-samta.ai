n = int(input("Enter the number: "))

a, b = 0, 1

print(f"Fibonacci Sequence up to {n} terms:", a, b, end=" ")

for i in range(2, n):
    a, b = b, a + b
    print(b, end=" ")

