#input
greeting=input('Greeting: ').lower()
# Get variables
hello=greeting.split()
h=hello[0].split('h')
#Checks
if hello[0]=='hello':
    print('$0')
elif h[0] == '':
    print('$20')
else:
    print('$100')
print(hello[0])
print(h[0])