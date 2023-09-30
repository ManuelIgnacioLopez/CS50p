import emoji
var=input("Input: ")
ok=0
try:
    print(f'Output: {emoji.emojize(var, language="alias")}')
    ok=True
finally:
    if ok != True:
        try:
            print(f'Output: {emoji.emojize(var)}')
        except Exception as e:
            ok=e

