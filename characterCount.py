message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
dict = {}
for character in message:
    dict.setdefault(character,0)
    dict[character] += 1
    
print(dict)
