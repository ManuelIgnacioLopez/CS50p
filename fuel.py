#Fuel Gauge
"""
This is a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
    and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again
"""

#prompt for X/Y
def main():
    while True:
        user_input= input("Fraction: ")
        try:
            a, b = user_input.split('/')
            try:
                if isint(a) and isint(b):
                    if int(a)<= int (b):
                        if int(b) != 0:
                            if int(a)/int(b) <= 1/100:
                                return print('E')
                            if int(a)/int(b) >= 99/100:
                                return print('F')
                            else:
                                return print(f"{round(int(a)/int(b)*100)}%")
            except Exception as e:
                return print(e)
        except ValueError:
            mistake='not using /'


#checks if str is fully int
def isint(string):
    numbers=["1","2","3","4","5","6","7","8","9","0"]
    for i in string:
        if i not in numbers:
            return False
    return True

main()