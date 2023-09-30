#grocery list
# iniciate list

#initiate it

#promt

def main():
    grocery_list=[]
    make_list(grocery_list)
    print_list(grocery_list)



#appends elements from user input to list
def make_list(grocery_list):
    while True:
        try:
            item=input()
            grocery_list.append(item.upper())
        except EOFError:
            print()
            return grocery_list.sort()

#list in order and result for user
def print_list(grocery_list):
    it=0
    for item in grocery_list:
        it+=1
        print(f"{it} {item}")

main()