#list of extensions
extensions=['.gif','.jpg','.jpeg','.png','.pdf','.txt','.zip']
# prompt user
file_name=input('File name: ')
found=False
for i in extensions:
    if file_name.find(i) != -1:
        j=i.replace('.','')
        print('image'+'/'+j, end='')
        found=True

if found == False:
    print("application/octet-stream")