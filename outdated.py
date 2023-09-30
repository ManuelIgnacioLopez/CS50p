# from english format to ISO 8601
#initialize c
c=True
# Months
Months = {
    "January": '01',
    "February": '02',
    "March": '03',
    "April": '04',
    "May": '05',
    "June": '06',
    "July": '07',
    "August": '08',
    "September": '09',
    "October": '10',
    "November": '11',
    "December": '12'
}
# prompt user
while c==True:
    user= input('Date: ').strip()
    if '/' in user:
        m,d,y=user.split('/')
    if int(d)<=31 and int(m)<=12:
        c=False
    else:
        m,d,y=user.split(' ')
        d=int(d)
        m=m.replace(',','')
        m=Months.get(m)
        if d<=31 and int(m)<=12:
            c=False
# create date with new format


if int(d)<=9:
    print(f"{y}-{m}-0{d}",end='')
else:
    print(f"{y}-{m}-{d}",end='')