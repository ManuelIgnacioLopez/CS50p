#grocery list
# iniciate list

#initiate it

#promt

def main():
    grocery_list={}
    make_list(grocery_list)
    print(grocery_list)
    print_list(grocery_list)



#appends elements from user input to list
def make_list(dicty):
    while True:
        try:
            item=input()

            if item.upper() not in dicty:
                dicty[item.upper()]=1
            else:
                dicty[item.upper()]+=1
        except EOFError:
            print()
            return dicty

#list in order and result for user
def print_list(dicty):

    temp_list = [key for key in dicty]
    temp_list= sorted(temp_list)
    for key in temp_list:
        print(f"{dicty.get(key)} {key}")


main()