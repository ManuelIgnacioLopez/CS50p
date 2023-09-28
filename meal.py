def main():
    time=input('What time is it? ')
    convert(time)



def convert(time):
    eat_times = ['breakfast time', 'lunch time', 'dinner time']
    hour=int(time.split(':')[0])
    #minutes=int(time.split(':')[1].split()[0])
    if 7<=hour<=8:
        return print(eat_times[0])
    elif 12<=hour<=13:
        return print(eat_times[1])
    elif 18<=hour<=19:
        return print(eat_times[2])
    else:
        return print()



if __name__ == "__main__":
    main()