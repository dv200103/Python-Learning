def collatz(n):
    while n != 1:
        print(n)
        if n%2==0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)

try:
    start = int(input('Enter a starting number for a collatz sequence.'))
    collatz(start)
except ValueError:
    print('Please enter a valid integer.')
