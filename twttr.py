#vowel substractor
vowels=['a','e','i','o','u']
#prompt
Input=input('Input: ')
Output=''
for l in Input:
    if l not in vowels:
        Output+=l

print(f'Output: {Output}')

