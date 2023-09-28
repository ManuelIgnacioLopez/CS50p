def main():
    eat_times = ['breakfast time', 'lunch time', 'dinner time']

    time=input('What time is it? ')
    hour=convert(time)

    if 7<=hour<=8:
        return print(eat_times[0])
    elif 12<=hour<=13:
        return print(eat_times[1])
    elif 18<=hour<=19:
        return print(eat_times[2])



def convert(time):
    hour=int(time.split(':')[0])
    minutes=int(time.split(':')[1].split()[0])
    return hour + int(minutes/60*100)/100




if __name__ == "__main__":
    main()