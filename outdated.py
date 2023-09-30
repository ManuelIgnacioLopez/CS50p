# from english format to ISO 8601
# Months
Months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
# prompt user
user= input('Date: ').strip()
if '/' in user:
    m,d,y=user.split('/')
else:
    m,d,y=user.split(' ')
    m=m.replace(',','')
    m=Months.get(m)
# create date with new format
print(f"{y}-{m}-{d}",end='')
