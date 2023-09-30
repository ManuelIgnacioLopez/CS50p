import emoji
try:
    print(f'Output: {emoji.emojize(input("Input: "), language="alias")}')
except Exception as e:
    'idk'
try:
    print(f'Output: {emoji.emojize(input("Input: "))}')
except Exception as e:
    'idk'
