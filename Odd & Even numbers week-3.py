a = int(input("Enter an integer (positive or negative): "))

if a > 0:
    print(f"The number {a} is positive")
elif a < 0:
    print(f"The number {a} is negative")
else:
    print(f"The number {a} is zero")

# Check even or odd (works for positive and negative numbers)
if a != 0:
    if a % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is even")
