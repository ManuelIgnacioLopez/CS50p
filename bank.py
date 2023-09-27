#input
greeting=input('Greeting: ').lower()
# Get variables
hello=greeting.find('hello')
h=greeting.find('h')
#Checks
if hello != -1 :
    print('$0')
elif h != -1 :
    print('$20')
else:
    print('$100')
