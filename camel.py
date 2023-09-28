#prompts for camel version
camelCase=input("camelCase: ")
#initiate snake variable
snake_case=''
#creates snake version
for letter in camelCase:
    if letter.islower():
        snake_case+=letter
    else:
        snake_case+= '_'+letter.lower()
#returns value
print(f'snake_case: {snake_case}')