num = int(input("Enter a number: "))
p = 0

for i in range(2, num):
    if (num % i == 0):
        p = 1

if p == 0:
    print(f"{num} is a prime number")
elif p == 1:
    print(f"{num} is not a prime number")
