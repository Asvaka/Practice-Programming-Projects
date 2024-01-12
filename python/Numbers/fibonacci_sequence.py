def fibonacci_sequence(n):
    if n < 0:
        print("incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

def main():
    print(fibonacci_sequence(int(input())))

main()