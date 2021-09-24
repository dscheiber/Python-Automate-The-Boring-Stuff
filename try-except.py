#this is a snip of code to practice a try and except block
#which functions as input validation

numCats = input('How many integers of cats do you have? \n')

try:
    integerCats = int(numCats)
    if(integerCats==1):
        print('You have', integerCats, "cat.")
    elif(integerCats>=0):
        print('You have', integerCats, "cats.")
    else:
        print('I\'m sorry for your loss.')    
except:
    print('That is not an integer of cats.')

    