# This program splits str and adds 3 dots between each word
Message = input('').split(' ')
it=0
show=''
for word in Message:
    it+=1
    if it < (len(Message)):
        show+=word + '...'
    else:
        show+= word

print(show)