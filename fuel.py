"""
pThis is a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
    and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again
"""

#prompt for X/Y
def main():
    try:
        a, b = input("Fraction: ").split('/')

    except Exception as e:
        return print(e)
    if isint(a) and isint(b):
        if b != 0:
            if a == 0:
                return print('E')
            if int(a)/int(b) == 1:
                return print('F')
            else:
                return print(f"{int(int(a)/int(b)*100)}%")
    else:
        return print(f"{a}/{b}")

def isint(string):
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    if string in numbers:
        return True
    else:
        return False
main()
