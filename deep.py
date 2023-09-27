#ask user
response=input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower()
#check
if response == '42' or response == 'forty-two' or response =='forty two':
    print('Yes')
else:
    print('No')