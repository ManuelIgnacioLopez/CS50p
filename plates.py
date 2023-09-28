#massachusetts plates validator
'''
restrictions taken into account:
1- “All vanity plates must start with at least two letters.”

2- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

3- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

4- “No periods, spaces, or punctuation marks are allowed.”
'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    cero=list()
    if 2<=len(s)<=6:
        if not is_int(s[0]) and not is_int(s[0]):
            for letter in s:
                if prohibited(letter):
                    return False
            for lettr in s:
                if is_int(lettr):
                    cero.append(str(lettr))
                    s=s.replace(lettr,'.')
            new_s=s.split('.')
            it=0
            for i in new_s:
                it+=1
                if i != '':
                    last=it
            if len(cero) == 0:
                cero=['There are no numbers','']

            if last==1 and cero[0] != '0':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def is_int(s):
    integers=['1','2','3','4','5','6','7','8','9','0']
    if s in integers:
        return True
    else:
        return False
def prohibited(s):
    proh=['.',' ','/,','!','?','/"',';',"/'",'/(','/)','/[','/]']
    if s in proh:
        return True
    else:
        return False



main()