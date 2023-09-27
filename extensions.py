#list of extensions
extensions=['.gif','.jpg','.jpeg','.png','.pdf','.txt','.zip']
# prompt user
file_name=input('File name: ')
found=False
for i in extensions:
    if file_name.find(i) != -1:
        j=i.replace('.','')
        if i == 'jpg':
            print('image/jpeg', end='')
            found=True
        elif i == 'txt':
            print('text/plain', end='')
            found=True
        elif i == 'pdf':
            print('application/pdf', end='')
            found=True
        elif i == 'zip':
            print('application/zip', end='')
            found=True
        else:
            print('image'+'/'+j, end='')
            found=True

if found == False:
    print("application/octet-stream")