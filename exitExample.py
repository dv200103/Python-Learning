'''from sys import*

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        exit()
    print('You typed ' + response + '.')'''



import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')    
