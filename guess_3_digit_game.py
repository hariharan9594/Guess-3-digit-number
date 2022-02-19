import random

#generate 3 digit number randomly:

def gen_num():
    x =['1','2','3','4','5','6','7','8','9','0']
    random.shuffle(x)
    return x[:3]

#guess 3 digit num:

def guess():
    g_num = list(input("Guess 3 digit number:\n"))
    return g_num


#compare two numbers:

def compare(a):
    if a == com_num:
        print("\nyou won the game...!\n")
        print("\ncomputer generated number is {}".format(com_num))
        return True
    else:
        clues(a)
#check for clues:

def clues(b):
    i=0
    if (b[i] == com_num[i] and b[i+1] == com_num[i+1])or(b[i+1] == com_num[i+1] and b[i+2] == com_num[i+2]):
        print("\n Too close to win..\n")
    elif b[i] == com_num[i] or b[i+1] == com_num[i+1] or b[i+2] == com_num[i+2] : 
        print("\n Match found.. try more")
    elif b!=com_num:
        print("\n Nope.. pls try new guess")
# or  b[i+1] == com_num[i+1] or  b[i+2] == com_num[i+2] :
#main Program:

com_num = gen_num()
while 1:
    #print(com_num)
    guess_num = guess()
    cycle = compare(guess_num)
    if cycle == True:
        break