#calculator screen and prompt
x,y,z=input('Expression: ').split()
x=float(x)
z=float(z)

if y=='+':
    print(float(x+z))
elif y=='/':
    print(float(x/z))
elif y=='*':
    print(float(x*z))
elif y=='-':
    print(float(x/z))
else:
    print('You made a mistake')

