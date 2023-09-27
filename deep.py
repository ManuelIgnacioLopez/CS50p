#ask user
response=input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower()

#check
if response.find('42') != -1 or response == 'forty-two' or response =='forty two':
    print('Yes')
else:
    print('No')