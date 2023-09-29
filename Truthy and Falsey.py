name = ''
while not name:
    print('Enter your name: ')
    name = input()
print('How many guest will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough rooms for all your guest.')
print('Done')

       #OR

'''name = ''
while not name != '':
    print('Enter your name: ')
    name = input()
print('How many guest will you have?')
numOfGuests = int(input())
if numOfGuests != 0:
    print('Be sure to have enough rooms for all your guest.')
print('Done')'''

        #OR

'''name = ''
while name == '':
    print('Enter your name: ')
    name = input()
print('How many guest will you have?')
numOfGuests = int(input())
if numOfGuests != 0:
    print('Be sure to have enough rooms for all your guest.')
print('Done')'''

