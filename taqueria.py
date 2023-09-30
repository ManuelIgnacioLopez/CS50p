# Felipe’s Taqueria

#Menu
Menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Total=0
while True:
    try:
        item=input('Item: ').title()
        Total+=float(round(Menu[item],1))
        print(f"Total: ${round(Total,1)}0")

    except (EOFError):
        print('')
        break
    except KeyError:
        try_again=True